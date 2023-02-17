import csv

a = []
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        s = row['Images']
        k = s.split('\n')
        for i in k:
            b = i.split(',')
            if len(b) > 3:
                a.append(row)

with open('result1.csv', 'w', encoding='utf-8') as b:
    writer = csv.writer(b)
    writer.writerow(a)
