# my first time using python

import serial
import sounddevice as sd
import numpy as np
import threading
import time

PORT = '/dev/ttyUSB0'
BAUDRATE = 115200
SAMPLE_RATE = 44100
DURATION = 0.01
THRESHOLD = 0.001

ser = serial.Serial(PORT, BAUDRATE)

def process_audio():
    while True:
        audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
        sd.wait()
        volume = np.max(np.abs(audio))

        print(f"volume: {volume: .3f}")

        if volume < THRESHOLD:
            brightness = 0
        else:
            brightness = int((volume - THRESHOLD) * 255 / (1 - THRESHOLD))
            brightness = max(0, min(brightness, 255))

        ser.write(f"{brightness}\n".encode())

threading.Thread(target=process_audio, daemon=True).start()

try:
    while True:
        time.sleep(0.01)
finally:
    ser.close()
