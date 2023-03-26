import json
from collections import defaultdict

phrases = defaultdict(list)
with open("task2_out.txt", "w", encoding="utf-8") as out:
    with open('RomeoAndJuliet.json', encoding="utf-8") as f:
        cur = json.load(f)
        for act in cur["acts"]:
            for scene in act["scenes"]:
                for action in scene["action"]:
                    phrases[action["character"]] += action["says"]
    for k, v in phrases.items():
        out.write(f"{k} says: {v}\n")
