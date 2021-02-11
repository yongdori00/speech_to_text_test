# https://gist.github.com/mabdrabo/8678538

import pyaudio
import wave
import cv2
 
FORMAT = pyaudio.paInt16
CHANNELS = 1  #only mono
RATE = 16000  
CHUNK = 1024  #확인 필요
RECORD_COMMAND = " " 

WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
try:
    while True:
        data = stream.read(CHUNK)
        frames.append(data)
except input() == RECORD_COMMAND:
    pass
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

print ("finished recording")
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()