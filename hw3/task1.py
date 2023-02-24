import json

words = {}
with open('wikidata_1000.json', encoding="utf-8") as f:
    for line in f.readlines():
        cur = json.loads(line)
        words[cur["label"]["value"]] = cur["description"]["value"] if "description" in cur else None

with open("task1_out.json", "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False)
