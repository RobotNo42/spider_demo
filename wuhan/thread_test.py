from threading import Thread
import time


def say(name):
    time.sleep(5)
    print(name)


if __name__ == '__main__':
    t1 = Thread(target=say,args=('jack',))
    t2 = Thread(target=say,args=('messi',))
    t1.start()
    t2.start()
    t2.join()
    print('我才是主线程')