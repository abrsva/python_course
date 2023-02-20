import csv

a = []
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    a.append(next(reader))
    for row in reader:
        k = row[-1]
        if 10000 < float(k) <= 50000:
            a.append(row)

with open('result2.csv', 'w', newline='', encoding='utf-8') as b:
    writer = csv.writer(b)
    writer.writerows(a)
