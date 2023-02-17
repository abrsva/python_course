import csv

a = {}
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        row.pop('Images')
        row.pop('Description')
        # a['Id'] = row['Id']
        # a['Title'] = row['Title']
        # a['Price'] = row['Price']

with open('result3.csv', 'w', encoding='utf-8') as d:
    fieldnames = row.keys()
    writer = csv.DictWriter(d, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(row)
