import csv

to_pop = ["Images", "Description"]
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    with open('result3.csv', 'w', newline='', encoding='utf-8') as d:
        header = list(reader.fieldnames)
        for field in to_pop:
            header.remove(field)
        writer = csv.DictWriter(d, delimiter=',', fieldnames=header)
        writer.writeheader()
        for row in reader:
            for field in to_pop:
                row.pop(field)
            writer.writerow(row)
