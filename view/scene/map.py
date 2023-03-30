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
            item["layer"] = 1
        elif name == "walls":
            item["mod_name"] = "wall"
            item["mod_index"] = 7
            item["layer"] = 0
        elif name == "wall":
            item["mod_name"] = "wall"
            item["mod_index"] = 2
            item["layer"] = 0
        elif name == "steels":
            item["mod_name"] = "wall"
            item["mod_index"] = 6
            item["layer"] = 0
        elif name == "symbol":
            item["mod_name"] = "symbol"
            item["mod_index"] = 1
            item["layer"] = 0
        elif name == "player1":
            item["mod_name"] = "player1"
            item["mod_index"] = 0
            item["layer"] = 0

        item["position"] = position
        return item
            
    def get_tank_items(self):
        # 地图编辑
        items = []
        items.append(self.get_tank_item("player1", [240, 720]))
        items.append(self.get_tank_item("glass", [0, 120]))
        items.append(self.get_tank_item("glass", [0, 540]))
        return items


    def export_map(self, module: str):
        data = {}
        data["scene_id"] = 0
        data["desc"] = "test"
        data["back_ground"] = ""
        if module == 'tank':
            data["items"] = self.get_tank_items()

        self.save(module, data)


if __name__ == '__main__':
    t = Test()
    t.print_all_size("tank")
