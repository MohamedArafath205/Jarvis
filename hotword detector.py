import struct
import pyaudio
import pvporcupine
import os

porcupine = None
paud = None
audio_stream = None

try:
    porcupine = pvporcupine.create(keywords=("hey siri", "jarvis")) #pvporcupine.KEYWORDS for all keywords
    paud = pyaudio.PyAudio()
    audio_stream = paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    while True:
        keyword = audio_stream.read(porcupine.frame_length)
        keyword = struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index = porcupine.process(keyword)
        if keyword_index>=0:
            print("hotword detected")
            os.startfile("C:\\Users\\Arafath\\OneDrive\\Desktop\\Python\\jarvis.py")
            

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()