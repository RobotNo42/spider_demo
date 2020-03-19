import time


def ss(x):
    def new_begin(func):
        def f1(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('run time id %s' % (end_time-start_time))
            print(x)
        return f1
    return new_begin


@ss(x='臭不要脸')
def try1(name, password):
    print(name, password)
    for i in range(100):
        if i%11 == 0:
            print(i)


try1('chengge1124',1124)
