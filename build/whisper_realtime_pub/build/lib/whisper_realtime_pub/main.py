import os
import whisper
from clear_folder import clean_folder
import numpy as np

def mic():
    model = whisper.load_model("small")

    path = './wav/'
    while 1:
        try:
            files = os.listdir(path)
            break
        except:
            continue

    clean_folder(path)

    while 1:
        files = os.listdir(path)
        if len(files) > 3:
            os.remove(path + files[0])
            os.remove(path + files[1])
            continue
        files = np.sort(files)
        for i in files:
            # print("a")
            result = model.transcribe(path + i, language="Chinese", no_speech_threshold=0.8, logprob_threshold=-1.6,
                                      temperature=0.4)
            # print("b")
            print(i + ': ' + result["text"])
            print(result["text"], file=open('result.txt', 'w'))
            os.remove(path + i)


if __name__ == '__main__':
    mic()
