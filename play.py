import os
import time
from pygame import mixer
from deepgram_tts import deepgram_tts
import threading

filepath = 'file path'
def play(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    thread = threading.Thread(target=check_and_remove, args=(file_path,))
    thread.start()

def sound_playing():
    return mixer.music.get_busy()

def stop_audio():
    mixer.music.stop()
    mixer.quit()

def check_and_remove(file_path):
    while True:
        if sound_playing():
            time.sleep(0.1)
        else:
            stop_audio()
            time.sleep(0.5)
            if os.path.exists(file_path):
                os.remove(file_path)
                print("Removed file")
            break

# TTS
def tts(text):
    length = len(text)
    lowercase_text = text.lower()
    if length < 2000:
        deepgram_tts(lowercase_text)
