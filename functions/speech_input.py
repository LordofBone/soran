import sounddevice as sd
from scipy.io.wavfile import write

from config.tensorflowasr import *

import logging

logger = logging.getLogger("listener")


def listen():
    """
    Listen to the microphone and return the recorded sound.
    :return:
    """

    fs = 16000
    seconds = 6

    sd.default.samplerate = fs
    sd.default.channels = 1
    sd.default.dtype = "int16"

    logger.debug("Listening...")

    audio_in = sd.rec(int(seconds * fs), blocking=True)

    logger.debug("Finished listening")

    write(str(audio_file), fs, audio_in)

    # todo: figure out how to get audio to record only on voice and end when voice is done


if __name__ == '__main__':
    print(sd.query_devices())
    print(listen())
