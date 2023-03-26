import csv
from collections import OrderedDict

adds = dict()
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for i, row in enumerate(reader):
        adds[row[2]] = float(row[-1])

with open("task4_out_ascending.txt", "w", encoding="utf-8") as out:
    adds = OrderedDict(sorted(adds.items(), key=lambda x: x[1]))
    for k, v in adds.items():
        out.write(f"{v}: {k}\n")

with open("task4_out_descending.txt", "w", encoding="utf-8") as out:
    for k, v in reversed(adds.items()):
        out.write(f"{v}: {k}\n")
