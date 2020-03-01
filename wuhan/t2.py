def res(x):
    print('welcome %s to shaxian res')
    menu_list = []
    while True:
        if menu_list == 0:
            print('nothing')
        else:
            print('目前吃了%s'% menu_list)
            food = yield menu_list
            print('%s start eat %s' % (x, food))
            menu_list.append(food)


f = res('汪梓成')
next(f)
f.send('蒸熊掌')
f.send('烧鹅')
f.send('蝙蝠')
f.send('蚕宝宝')
f.send('不吃了')