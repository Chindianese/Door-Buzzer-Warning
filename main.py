# Print out realtime audio volume as ascii bars

import sounddevice as sd
import numpy as np
from win10toast import ToastNotifier
import datetime
import beepy
import requests
import soundtest
toaster = ToastNotifier()

duration = 200000  # seconds
bufferDuration = 20

global triggerTime
global startTime


def NotifyBot():
    url = 'http://localhost:3001/doorAlert'
    myobj = {'somekey': 'somevalue'}

    x = requests.post(url, data=myobj)
    print(x.text)


def datetime_to_float():
    # d = datetime.datetime.now().time()
    #epoch = datetime.datetime.utcfromtimestamp(0)
    #total_seconds = (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return datetime.datetime.now().timestamp()


triggerTime = 0
startTime = datetime_to_float()

global counter
counter = 0


def print_sound(in_data, out_data, frames, time, status):
    volume_norm = np.linalg.norm(in_data)*10
    # print("|" * int(volume_norm))
    #if volume_norm > 0:
        #print(volume_norm)
    global triggerTime
    time = datetime_to_float()
    # print (time-startTime)
    global counter
    if 12 <= volume_norm < 25 and (time - triggerTime) > bufferDuration and (time - startTime) > 2:
        counter = counter + 1
        print('$', counter, '-', volume_norm)
        if counter > 13:
            print(int(volume_norm))
            triggerTime = datetime_to_float()
            print("Alert")
            beepy.beep(sound=3) # integer as argument
            toaster.show_toast("LIONEL ALERT", "Buzzer was heard")
            counter = 0
            # soundtest.SASAGEYO()
            # NotifyBot()
    else:
        counter = 0


# NotifyBot()
print("Started")
with sd.Stream(callback=print_sound):
    sd.sleep(duration * 10000)
toaster.show_toast("LIONEL ALERT", "Going to sleep")
print("Ended")