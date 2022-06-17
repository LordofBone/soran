from tensorflow_asr.utils import env_util

from config.tensorflowasr import *

import tensorflow as tf

env_util.setup_devices([device], cpu=cpu)

from tensorflow_asr.configs.config import Config
from tensorflow_asr.featurizers.speech_featurizers import read_raw_audio
from tensorflow_asr.featurizers.speech_featurizers import TFSpeechFeaturizer
from tensorflow_asr.featurizers.text_featurizers import SubwordFeaturizer
from tensorflow_asr.models.transducer.conformer import Conformer
from tensorflow_asr.utils.data_util import create_inputs


# thanks to: https://github.com/TensorSpeech/TensorFlowASR
class SpeechInference(object):
    def __init__(self):
        """
        Initialize the speech inference class.
        """
        try:
            config = Config(config_file)
            self.speech_featurizer = TFSpeechFeaturizer(config.speech_config)

            self.text_featurizer = SubwordFeaturizer.load_from_file(config.decoder_config, subwords_file)

            self.text_featurizer.decoder_config.beam_width = beam_width

            # build model
            self.conformer = Conformer(**config.model_config, vocabulary_size=self.text_featurizer.num_classes)
            self.conformer.make(self.speech_featurizer.shape)
            self.conformer.load_weights(model, by_name=True, skip_mismatch=True)
            self.conformer.summary(line_length=120)
            self.conformer.add_featurizers(self.speech_featurizer, self.text_featurizer)

        except Exception as e:
            print("Please download the models from Google Drive using utils/model_downloader.py")
            exit(1)

    def run_stt(self):
        """
        Run speech inference.
        :return:
        """
        signal = read_raw_audio(audio_file)
        features = self.speech_featurizer.tf_extract(signal)
        input_length = tf.shape(features)[0]

        if beam_width:
            inputs = create_inputs(features[None, ...], input_length[None, ...])
            transcript = self.conformer.recognize_beam(inputs)
        elif timestamp:
            transcript, stime, etime, _, _ = self.conformer.recognize_tflite_with_timestamp(
                signal, tf.constant(self.text_featurizer.blank, dtype=tf.int32),
                self.conformer.predict_net.get_initial_state()
            )
        else:
            code_points, _, _ = self.conformer.recognize_tflite(
                signal, tf.constant(self.text_featurizer.blank, dtype=tf.int32),
                self.conformer.predict_net.get_initial_state()
            )
            return tf.strings.unicode_encode(code_points, "UTF-8").numpy().decode("UTF-8")


SpeechInferencer = SpeechInference()

if __name__ == "__main__":
    print(SpeechInferencer.run_stt())
