# --*-- utf-8 --*--

import sounddevice as sd
import numpy as np
import pyautogui
import time
import win32gui
import autoit

Duration = 7200  # 秒間収音する
ThresholdChangeToShy = 8.0e-3
ThresholdChangeToSmile = 1.0e-3

device_list = sd.query_devices()
print(device_list)

def changeLook(looks: str):
    if looks == "Smile": looksNumber = "1"
    if looks == "Sad": looksNumber = "2"
    if looks == "Shy": looksNumber = "3"


    memoapp = win32gui.FindWindow(None,'Puppet3G')
    time.sleep(1)
    try:
        win32gui.SetForegroundWindow(memoapp)
    finally:
        pass

    lookKey = "!" + looksNumber
    autoit.send(lookKey)
    return()

def callback(indata, frames, time, status):
    if np.sqrt(np.mean(indata**2)) > ThresholdChangeToShy:
        changeLook("Shy")
    if np.sqrt(np.mean(indata**2)) < ThresholdChangeToSmile:
        changeLook("Smile")

with sd.InputStream(
        channels=1, 
        dtype='float32', 
        callback=callback
    ):
    sd.sleep(int(Duration * 1000))
    