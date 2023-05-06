import sounddevice as sd
from scipy.io.wavfile import write
import time
from clear_folder import clean_folder
import numpy as np
import os

class Queue:
    def __init__(self, size):
        # self.q = np.zeros((5, 1, 2))
        self.q = [[[0, 0]] for i in range(size)]
        self.size = size
        self.front = size-1
        self.rear = size-1
        self.is_full_index = False

    def enqueue(self, element):
        if self.isFull():
            self.rear = (self.rear+1) % self.size
            self.front = (self.front+1) % self.size
            # print(self.rear)
            self.q[self.rear] = element
            return
        self.rear = (self.rear+1) % self.size
        print(self.rear)
        self.q[self.rear] = element
        if self.front == self.rear:
            self.is_full_index = True
        return

    def dequeue(self):
        self.is_full_index = False
        if self.isEmpty():
            return
        self.front = (self.front+1) % self.size
        return

    def isFull(self):
        if (self.front == self.rear) and (self.is_full_index is True):
            return 1
        else:
            return 0

    def isEmpty(self):
        if (self.front == self.rear) and (self.is_full_index is False):
            return 1
        else:
            return 0

def record(length):
    concatenated_segments_in_wav = 2
    fs = 16000  # Sample rate
    seconds = float(length)  # Duration of recording
    recording = Queue(concatenated_segments_in_wav)

    path = './wav/'
    try:
        files = os.listdir(path)
    except:
        os.mkdir(path)

    clean_folder(path)

    for i in range(recording.size-1):
        recording.enqueue(sd.rec(int(seconds * fs), samplerate=fs, channels=2))
        sd.wait()  # Wait until recording is finished
    while 1:
        recording.enqueue(sd.rec(int(seconds * fs), samplerate=fs, channels=2))
        sd.wait()  # Wait until recording is finished
        # print(recording.q[0])
        wav = np.concatenate(recording.q, axis=0)
        print(wav)
        # wav = scipy.vstack((recording.q[0], recording.q[1]))
        current_t = str(int(time.time() * 100))
        write(path + 'output_' + current_t + '.wav', fs, wav)  # Save as WAV file
        print("output_" + current_t + ".wav: {:.1f}s recording finished.".format(seconds))



if __name__ == '__main__':
    length = 1.5
    record(length)
