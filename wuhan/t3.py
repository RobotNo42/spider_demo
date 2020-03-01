import random


def test():
    s = ''
    for i in range(5):
        s1 = chr(random.randint(65, 90))
        s2 = chr(random.randint(97, 122))
        s3 = random.randint(0,9)
        s_all = random.choice([s1, s2, str(s3)])
        s += s_all
    return s

d = test()
print(d)