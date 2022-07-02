from functions.run_speech_inference import SpeechInferencer
from functions.speech_input import listen

import logging


class SpeechtoTextHandler:
    def __init__(self):
        self.listening = False
        self.inferencing = False

    def initiate_recording(self):
        """
        Initiate recording.
        :return:
        """
        self.listening = True

        listen()

        self.listening = False

    def run_inference(self):
        """
        Run speech inference.
        :return:
        """
        self.inferencing = True

        text_output = SpeechInferencer.run_stt()

        self.inferencing = False

        return text_output


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    SpeechtoTextTest = SpeechtoTextHandler()
    SpeechtoTextTest.initiate_recording()
    print(SpeechtoTextTest.run_inference())
