import csv
with open('stock.csv','r',encoding='gbk') as f:
    reader = csv.reader(f)

    for i in reader:
        print(i)