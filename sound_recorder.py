# https://gist.github.com/mabdrabo/8678538

import pyaudio
import wave
import threading as th

FORMAT = pyaudio.paInt16
CHANNELS = 1  #only mono
RATE = 16000  
CHUNK = 1024  #확인 필요
RECORD_COMMAND = ' '

keep_going = True
def key_capture_thread():
    global keep_going
    input()
    keep_going = False

def do_stuff():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
    print("press space bar to finish")
    while keep_going:
        data = stream.read(CHUNK)
        frames.append(data)

WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []

do_stuff()
 
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