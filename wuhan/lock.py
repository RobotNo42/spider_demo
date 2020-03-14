import threading
import time


num = 100
R = threading.Lock()


def AddNum():
    R.acquire()
    global num
    temp = num
    time.sleep(0.2)
    num = temp-1
    R.release()


thread_list = []
for i in range(100):
    t = threading.Thread(target=AddNum)
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
print('num is %d'% num)