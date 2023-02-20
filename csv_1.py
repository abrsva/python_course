import csv

a = []
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        imags = row["Images"].split(",")
        if len(imags) > 3:
            a.append(row)

with open('result1.csv', 'w', newline='', encoding='utf-8') as d:
    writer = csv.DictWriter(d, delimiter=',', fieldnames=a[0].keys())
    writer.writeheader()
    writer.writerows(a)
