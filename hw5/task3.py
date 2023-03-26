import json
from collections import Counter

phrases = Counter()
with open('RomeoAndJuliet.json', encoding="utf-8") as f:
    cur = json.load(f)
    for act in cur["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                phrases += Counter([action["character"]] * len(action["says"]))
    print(phrases.most_common())
