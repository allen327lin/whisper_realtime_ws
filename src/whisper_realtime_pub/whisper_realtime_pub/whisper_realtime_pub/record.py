import sounddevice as sd
from scipy.io.wavfile import write

def record(length):
    fs = 16000  # Sample rate
    seconds = float(length)  # Duration of recording
    i = 1
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('./wav/output'+str(i)+'.wav', fs, recording)  # Save as WAV file

    print("{:.1f}s recording finished.".format(seconds))
    i += 1
