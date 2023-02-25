import csv

with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    with open('result1.csv', 'w', newline='', encoding='utf-8') as d:
        writer = csv.DictWriter(d, delimiter=',', fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            imags = row["Images"].split(",")
            if len(imags) > 3:
                writer.writerow(row)
