from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import pyaudio
import json
import pyttsx3
from core import SystemCore

SetLogLevel(0)

if not os.path.exists('model'):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

sample_rate=41100
model = Model('model')
rec = KaldiRecognizer(model, sample_rate)

audio = pyaudio.PyAudio()
engine = pyttsx3.init()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=41000, input=True, frames_per_buffer=8000)
stream.start_stream()

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    data = stream.read(8192)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        if result is not None:
            text = result['text']
            print(text)
            if text == 'são que horas':
                speak(SystemCore.get_time())