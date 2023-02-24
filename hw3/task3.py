import json
from collections import defaultdict

cnt = defaultdict(int)
with open('RomeoAndJuliet.json', encoding="utf-8") as f:
    cur = json.load(f)
    with open("task2_out.json", "w", encoding="utf-8") as out:
        for act in cur["acts"]:
            for scene in act["scenes"]:
                for action in scene["action"]:
                    cnt[action["character"]] += 1
print(max(cnt.items(), key=lambda x: x[1])[0])
