import csv
from collections import Counter

cnt = Counter()
lines_to_read = 4444
punctuation = ",:;\"«»—-\r\t\n()<>[]/+1234567890."
with open('stage3_test.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for i, row in enumerate(reader):
        cnt += Counter(
            (row[2] + " " + row[3]).translate(str.maketrans({sep: " " for sep in punctuation})).split()
        )
        if i >= lines_to_read:
            break

print('20 самых частых слов: ', *map(lambda x: x[0], cnt.most_common(20)))
print('20 самых редких слов: ', *map(lambda x: x[0], sorted(cnt.items(), key=lambda x: x[1])[:20]))
