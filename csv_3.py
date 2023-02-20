import csv

with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    a = list(reader)
    for row in a:
        row.pop('Images')
        row.pop('Description')

with open('result3.csv', 'w', newline='', encoding='utf-8') as d:
    writer = csv.DictWriter(d, delimiter=',', fieldnames=a[0].keys())
    writer.writeheader()
    writer.writerows(row)
