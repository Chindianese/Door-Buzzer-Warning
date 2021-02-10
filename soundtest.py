import sounddevice as sd
import soundfile as sf


def SASAGEYO():
    filename = 'sasageyo.wav'
    sd.default.device = 4
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    # status = sd.wait()  # Wait until file is done playing


# SASAGEYO()