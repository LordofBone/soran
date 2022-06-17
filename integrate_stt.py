from functions.run_speech_inference import SpeechInferencer
from functions.speech_input import listen


def run_stt_inference():
    """
    Run speech inference.
    :return:
    """
    listen()
    return SpeechInferencer.run_stt()


if __name__ == '__main__':
    print(run_stt_inference())
