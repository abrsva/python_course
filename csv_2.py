import csv

a = []
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        k = row[-1]
        a.append(k)
new = []
a.remove('Price')
for i in a:
    if 10000.0 < float(i) < 50000.0:
        new.append(i)

with open('result2.csv', 'w') as b:
    writer = csv.writer(b)
    writer.writerow(new)
