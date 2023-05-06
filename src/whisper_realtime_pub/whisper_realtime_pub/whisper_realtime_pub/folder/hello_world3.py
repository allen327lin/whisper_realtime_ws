import time

def hello_world3():
    i = 1
    while 1:
        print("Hello, world3. {}".format(i))
        i += 1
        time.sleep(1)

if __name__ == '__main__':
    hello_world3()