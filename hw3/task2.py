import json

with open('RomeoAndJuliet.json', encoding="utf-8") as f:
    cur = json.load(f)
    with open("task2_out.json", "w", encoding="utf-8") as out:
        for act in cur["acts"]:
            for scene in act["scenes"]:
                characters = set()
                for action in scene["action"]:
                    characters.add(action["character"])
                out.write(json.dumps({"characters": list(characters)}))
                out.write("\n")
