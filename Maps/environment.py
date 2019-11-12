import json


class Environment:
    def __init__(self, map_name):
        self.file_path = "Maps/"+map_name+".json"
        file = open(self.file_path, "r", encoding="utf-8")
        data = json.load(file)
        self.terrain = data["terrain_data"]
        file.close()

    def object_at_location(self, y, x):
        if self.terrain[x][y] != " ":
            return True
        else:
            return False

    def change_map_to(self, map_name):
        self.file_path = "Maps/"+map_name+".json"
        file = open(self.file_path, "r", encoding="utf-8")
        data = json.load(file)
        self.terrain = data["terrain_data"]
        file.close()

    def get_map(self):
        map_string = "".join(self.terrain)
        return map_string
