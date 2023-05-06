import os

def clean_folder(path):
    if path[-1:] != '/':
        path = path+'/'
    for i in os.listdir(path):
        os.remove(path + i)

if __name__ == '__main__':
    path = './wav/'
    clean_folder(path)