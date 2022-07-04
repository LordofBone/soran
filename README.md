### What is Soran?
This is a project I have made built around [TensorflowASR](https://github.com/TensorSpeech/TensorFlowASR) 
speech recognition engine.

This should work on both Windows x86_64 and Linux x86_64 and Raspberry Pi (test on a Pi 4 running 64 Bit RPi OS).

It is called Soran based off of the Star Trek character, [Soran](https://memory-alpha.fandom.com/wiki/Tolian_Soran).

##### What is TensorflowASR?
TensorflowASR is a speech recognition engine that is built on top of Google's [TensorFlow](https://www.tensorflow.org/) 
framework.

It allows for local (offline) speech recognition, so you don't have to connect to an online API to perform decent 
speech recognition.

I have made this so that I can integrate into other projects such as my upcoming T-800 project. My previous projects 
[Nvidianator](https://www.hackster.io/314reactor/the-nvidianator-341f7a) and 
[EDITH glasses](https://www.hackster.io/314reactor/e-d-i-t-h-glasses-5604fa) used 
[wit.ai](https://wit.ai/) to perform speech recognition; which is effective; but of course requires API keys and
internet access.

##### Running Soran
Install the requirements with:
`pip install -r requirements.txt`

Run soran/utils/model_dowloader.py to get the pre-trained conformer model.

Then you can run integrate_stt.py and seeing if it can translate speech to text (ensure you have a microphone).

##### Integrating Soran into a project
If you want to integrate Soran into another system, such as a robot - you can pull down the repo into the folder of
the project you are working on, then append the system path of the Soran folder to the system path of the project.

`soran_dir = os.path.join( path_to_soran )`

`sys.path.append(soran_dir)`

You will also need to install everything in requirements.txt and/or add the requirements to your project's requirements.txt

If you are running on RPi you will need to remove the Tensorflow entries from the requirements.txt file and install
it manually as it currently does not appear to be on the pip index.

Follow the instructions here to install Tensorflow on RPi:
Download the wheel for 2.7.0 Python 3 64 Bit ARM: https://github.com/Qengineering/TensorFlow-Raspberry-Pi_64-bit

Then while still in the venv made above:

`PIP_EXTRA_INDEX_URL=https://snapshots.linaro.org/ldcg/python-cache/`

`pip3 install tensorflow-2.7.0-cp39-cp39-linux_aarch64.whl`

The index URL is to include tensorflow-io which is required as per the issue here: 
https://github.com/tensorflow/io/issues/1441

and it grabs that wheel from: https://snapshots.linaro.org/ldcg/python-cache/

And this should install all dependencies.

You can then go into the folder soran/utils and run model_dowloader.py to get the pre-trained conformer model.

Then you can run a test by running integrate_stt.py and seeing if it can translate speech to text 
(ensure you have a microphone).

Then importing SpeechInference from integrate_stt.py:
`from soran.integrate_stt import SpeechtoTextHandler`
Which can then be called from the program to record audio and get the text output.
`SpeechtoText = SpeechtoTextHandler()`
`SpeechtoText.initiate_recording()`
`print(SpeechtoText.run_inference())

Also the status of listening inferencing can be obtained from the class:
`print(SpeechtoTextTest.inferencing)`
`print(SpeechtoTextTest.listening)`