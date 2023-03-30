import pygame
import json
import os


class Test(object):

    def __init__(self):
        pass

    def save(self, module, data):
        with open(f"./{module}.json", "w") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def print_size(self, path: str):
        img = pygame.image.load(path)
        rect = img.get_rect()
        print(f"path: {path} - width: {rect.width}, height: {rect.height}")

    def print_all_size(self, module: str):
        for root, dirs, files in os.walk('../resource/' + module + '/image'):
            if dirs:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                self.print_size(file_path)

    def get_tank_item(self, name, position):
        item = {}
        if name == "glass":
            item["mod_name"] = "wall"
            item["mod_index"] = 0
            item["layer"] = 2
        elif name == "walls":
            item["mod_name"] = "wall"
            item["mod_index"] = 7
            item["layer"] = 1
        elif name == "wall":
            item["mod_name"] = "wall"
            item["mod_index"] = 2
            item["layer"] = 1
        elif name == "water":
            item["mod_name"] = "wall"
            item["mod_index"] = 1
            item["layer"] = 0
        elif name == "steels":
            item["mod_name"] = "wall"
            item["mod_index"] = 6
            item["layer"] = 1
        elif name == "symbol":
            item["mod_name"] = "symbol"
            item["mod_index"] = 1
            item["layer"] = 1
        elif name == "player1":
            item["mod_name"] = "player1"
            item["mod_index"] = 0
            item["layer"] = 1

        item["position"] = position
        return item
            
    def get_tank_items(self):
        # 地图编辑
        items = []

        items.append(self.get_tank_item("", [0, 0]))
        items.append(self.get_tank_item("", [0, 60]))
        items.append(self.get_tank_item("glass", [0, 120]))
        items.append(self.get_tank_item("walls", [0, 180]))
        items.append(self.get_tank_item("walls", [0, 240]))
        items.append(self.get_tank_item("water", [0, 300]))
        items.append(self.get_tank_item("water", [0, 360]))
        items.append(self.get_tank_item("walls", [0, 420]))
        items.append(self.get_tank_item("walls", [0, 480]))
        items.append(self.get_tank_item("glass", [0, 540]))
        items.append(self.get_tank_item("", [0, 600]))
        items.append(self.get_tank_item("", [0, 660]))
        items.append(self.get_tank_item("", [0, 720]))

        items.append(self.get_tank_item("", [60, 0]))
        items.append(self.get_tank_item("", [60, 60]))
        items.append(self.get_tank_item("", [60, 120]))
        items.append(self.get_tank_item("glass", [60, 180]))
        items.append(self.get_tank_item("walls", [60, 240]))
        items.append(self.get_tank_item("water", [60, 300]))
        items.append(self.get_tank_item("walls", [60, 360]))
        items.append(self.get_tank_item("walls", [60, 420]))
        items.append(self.get_tank_item("walls", [60, 480]))
        items.append(self.get_tank_item("water", [60, 540]))
        items.append(self.get_tank_item("glass", [60, 600]))
        items.append(self.get_tank_item("", [60, 660]))
        items.append(self.get_tank_item("", [60, 720]))

        items.append(self.get_tank_item("", [120, 0]))
        items.append(self.get_tank_item("", [120, 60]))
        items.append(self.get_tank_item("", [120, 120]))
        items.append(self.get_tank_item("glass", [120, 180]))
        items.append(self.get_tank_item("walls", [120, 240]))
        items.append(self.get_tank_item("water", [120, 300]))
        items.append(self.get_tank_item("walls", [120, 360]))
        items.append(self.get_tank_item("walls", [120, 420]))
        items.append(self.get_tank_item("water", [120, 480]))
        items.append(self.get_tank_item("water", [120, 540]))
        items.append(self.get_tank_item("glass", [120, 600]))
        items.append(self.get_tank_item("", [120, 660]))
        items.append(self.get_tank_item("", [120, 720]))

        items.append(self.get_tank_item("", [180, 0]))
        items.append(self.get_tank_item("", [180, 60]))
        items.append(self.get_tank_item("glass", [180, 120]))
        items.append(self.get_tank_item("walls", [180, 180]))
        items.append(self.get_tank_item("walls", [180, 240]))
        items.append(self.get_tank_item("walls", [180, 300]))
        items.append(self.get_tank_item("walls", [180, 360]))
        items.append(self.get_tank_item("water", [180, 420]))
        items.append(self.get_tank_item("water", [180, 480]))
        items.append(self.get_tank_item("glass", [180, 540]))
        items.append(self.get_tank_item("", [180, 600]))
        items.append(self.get_tank_item("", [180, 660]))
        items.append(self.get_tank_item("", [180, 720]))

        items.append(self.get_tank_item("", [240, 0]))
        items.append(self.get_tank_item("walls", [240, 60]))
        items.append(self.get_tank_item("walls", [240, 120]))
        items.append(self.get_tank_item("walls", [240, 180]))
        items.append(self.get_tank_item("steels", [240, 240]))
        items.append(self.get_tank_item("walls", [240, 300]))
        items.append(self.get_tank_item("walls", [240, 360]))
        items.append(self.get_tank_item("walls", [240, 420]))
        items.append(self.get_tank_item("water", [240, 480]))
        items.append(self.get_tank_item("glass", [240, 540]))
        items.append(self.get_tank_item("", [240, 600]))
        items.append(self.get_tank_item("", [240, 660]))
        items.append(self.get_tank_item("player1", [240, 720]))

        items.append(self.get_tank_item("", [300, 0]))
        items.append(self.get_tank_item("", [300, 60]))
        items.append(self.get_tank_item("glass", [300, 120]))
        items.append(self.get_tank_item("walls", [300, 180]))
        items.append(self.get_tank_item("walls", [300, 240]))
        items.append(self.get_tank_item("walls", [300, 300]))
        items.append(self.get_tank_item("walls", [300, 360]))
        items.append(self.get_tank_item("walls", [300, 420]))
        items.append(self.get_tank_item("walls", [300, 480]))
        items.append(self.get_tank_item("glass", [300, 540]))
        items.append(self.get_tank_item("", [300, 600]))
        items.append(self.get_tank_item("", [300, 660]))

        items.append(self.get_tank_item("", [360, 0]))
        items.append(self.get_tank_item("", [360, 60]))
        items.append(self.get_tank_item("walls", [360, 120]))
        items.append(self.get_tank_item("walls", [360, 180]))
        items.append(self.get_tank_item("steels", [360, 240]))
        items.append(self.get_tank_item("walls", [360, 300]))
        items.append(self.get_tank_item("walls", [360, 360]))
        items.append(self.get_tank_item("walls", [360, 420]))
        items.append(self.get_tank_item("water", [360, 480]))
        items.append(self.get_tank_item("glass", [360, 540]))
        items.append(self.get_tank_item("", [360, 600]))
        items.append(self.get_tank_item("wall", [345, 705]))
        items.append(self.get_tank_item("wall", [345, 720]))
        items.append(self.get_tank_item("wall", [345, 735]))
        items.append(self.get_tank_item("wall", [345, 750]))
        items.append(self.get_tank_item("wall", [345, 765]))
        items.append(self.get_tank_item("wall", [360, 705]))
        items.append(self.get_tank_item("wall", [375, 705]))
        items.append(self.get_tank_item("wall", [390, 705]))
        items.append(self.get_tank_item("wall", [405, 705]))
        items.append(self.get_tank_item("wall", [420, 705]))
        items.append(self.get_tank_item("wall", [420, 720]))
        items.append(self.get_tank_item("wall", [420, 735]))
        items.append(self.get_tank_item("wall", [420, 750]))
        items.append(self.get_tank_item("wall", [420, 765]))
        items.append(self.get_tank_item("symbol", [360, 720]))

        items.append(self.get_tank_item("", [420, 0]))
        items.append(self.get_tank_item("", [420, 60]))
        items.append(self.get_tank_item("glass", [420, 120]))
        items.append(self.get_tank_item("walls", [420, 180]))
        items.append(self.get_tank_item("walls", [420, 240]))
        items.append(self.get_tank_item("walls", [420, 300]))
        items.append(self.get_tank_item("walls", [420, 360]))
        items.append(self.get_tank_item("water", [420, 420]))
        items.append(self.get_tank_item("water", [420, 480]))
        items.append(self.get_tank_item("glass", [420, 540]))
        items.append(self.get_tank_item("", [420, 600]))
        items.append(self.get_tank_item("", [420, 660]))

        items.append(self.get_tank_item("", [480, 0]))
        items.append(self.get_tank_item("", [480, 60]))
        items.append(self.get_tank_item("", [480, 120]))
        items.append(self.get_tank_item("glass", [480, 180]))
        items.append(self.get_tank_item("walls", [480, 240]))
        items.append(self.get_tank_item("water", [480, 300]))
        items.append(self.get_tank_item("walls", [480, 360]))
        items.append(self.get_tank_item("walls", [480, 420]))
        items.append(self.get_tank_item("water", [480, 480]))
        items.append(self.get_tank_item("water", [480, 540]))
        items.append(self.get_tank_item("glass", [480, 600]))
        items.append(self.get_tank_item("", [480, 660]))
        items.append(self.get_tank_item("", [480, 720]))

        items.append(self.get_tank_item("", [540, 0]))
        items.append(self.get_tank_item("", [540, 60]))
        items.append(self.get_tank_item("", [540, 120]))
        items.append(self.get_tank_item("glass", [540, 180]))
        items.append(self.get_tank_item("walls", [540, 240]))
        items.append(self.get_tank_item("water", [540, 300]))
        items.append(self.get_tank_item("walls", [540, 360]))
        items.append(self.get_tank_item("walls", [540, 420]))
        items.append(self.get_tank_item("walls", [540, 480]))
        items.append(self.get_tank_item("water", [540, 540]))
        items.append(self.get_tank_item("glass", [540, 600]))
        items.append(self.get_tank_item("", [540, 660]))
        items.append(self.get_tank_item("", [540, 720]))

        items.append(self.get_tank_item("", [600, 0]))
        items.append(self.get_tank_item("", [600, 60]))
        items.append(self.get_tank_item("glass", [600, 120]))
        items.append(self.get_tank_item("walls", [600, 180]))
        items.append(self.get_tank_item("walls", [600, 240]))
        items.append(self.get_tank_item("water", [600, 300]))
        items.append(self.get_tank_item("water", [600, 360]))
        items.append(self.get_tank_item("walls", [600, 420]))
        items.append(self.get_tank_item("walls", [600, 480]))
        items.append(self.get_tank_item("glass", [600, 540]))
        items.append(self.get_tank_item("", [600, 600]))
        items.append(self.get_tank_item("", [600, 660]))
        items.append(self.get_tank_item("", [600, 720]))

        items.append(self.get_tank_item("", [660, 0]))
        items.append(self.get_tank_item("", [660, 60]))
        items.append(self.get_tank_item("", [660, 120]))
        items.append(self.get_tank_item("glass", [660, 180]))
        items.append(self.get_tank_item("glass", [660, 240]))
        items.append(self.get_tank_item("glass", [660, 300]))
        items.append(self.get_tank_item("water", [660, 360]))
        items.append(self.get_tank_item("glass", [660, 420]))
        items.append(self.get_tank_item("water", [660, 480]))
        items.append(self.get_tank_item("water", [660, 540]))
        items.append(self.get_tank_item("glass", [660, 600]))
        items.append(self.get_tank_item("", [660, 660]))
        items.append(self.get_tank_item("", [660, 720]))

        items.append(self.get_tank_item("", [720, 0]))
        items.append(self.get_tank_item("", [720, 60]))
        items.append(self.get_tank_item("", [720, 120]))
        items.append(self.get_tank_item("", [720, 180]))
        items.append(self.get_tank_item("", [720, 240]))
        items.append(self.get_tank_item("", [720, 300]))
        items.append(self.get_tank_item("glass", [720, 360]))
        items.append(self.get_tank_item("glass", [720, 420]))
        items.append(self.get_tank_item("water", [720, 480]))
        items.append(self.get_tank_item("glass", [720, 540]))
        items.append(self.get_tank_item("", [720, 600]))
        items.append(self.get_tank_item("", [720, 660]))
        items.append(self.get_tank_item("", [720, 720]))
        return items


    def export_map(self, module: str):
        maps = []
        data = {}
        data["scene_id"] = 0
        data["desc"] = "test"
        data["back_ground"] = ""
        if module == 'tank':
            data["items"] = self.get_tank_items()

        maps.append(data)
        self.save(module, maps)


if __name__ == '__main__':
    t = Test()
    # t.print_all_size("tank")
    t.export_map("tank")
