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
        if name == "grass":
            item["model"] = {}
            item["model"]["model_name"] = "grass"
            item["model"]["model_index"] = "grass"
            item["box_collider"] = {}
            item["box_collider"]["layer"] = 2
            item["box_collider"]["height"] = 60
            item["box_collider"]["width"] = 60
            item["transform"] = {}
            item["transform"]["position"] = [position[0] + 30, position[1] + 30]
        elif name == "walls":
            item["model"] = {}
            item["model"]["model_name"] = "wall"
            item["model"]["model_index"] = "walls"
            item["box_collider"] = {}
            item["box_collider"]["layer"] = 1
            item["box_collider"]["height"] = 60
            item["box_collider"]["width"] = 60
            item["transform"] = {}
            item["transform"]["position"] = [position[0] + 30, position[1] + 30]
        elif name == "wall":
            item["model"] = {}
            item["model"]["model_name"] = "wall"
            item["model"]["model_index"] = "wall"
            item["box_collider"] = {}
            item["box_collider"]["layer"] = 1
            item["box_collider"]["height"] = 15
            item["box_collider"]["width"] = 15
            item["transform"] = {}
            item["transform"]["position"] = [position[0] + 7, position[1] + 7]
        elif name == "water":
            item["model"] = {}
            item["model"]["model_name"] = "water"
            item["model"]["model_index"] = "water"
            item["box_collider"] = {}
            item["box_collider"]["layer"] = 0
            item["box_collider"]["height"] = 60
            item["box_collider"]["width"] = 60
            item["transform"] = {}
            item["transform"]["position"] = [position[0] + 30, position[1] + 30]
        elif name == "iron":
            item["model"] = {}
            item["model"]["model_name"] = "iron"
            item["model"]["model_index"] = "irons"
            item["box_collider"] = {}
            item["box_collider"]["layer"] = 1
            item["box_collider"]["height"] = 60
            item["box_collider"]["width"] = 60
            item["transform"] = {}
            item["transform"]["position"] = [position[0] + 30, position[1] + 22]
        elif name == "symbol":
            item["model"] = {}
            item["model"]["model_name"] = "symbol"
            item["model"]["model_index"] = "symbol"
            item["box_collider"] = {}
            item["box_collider"]["layer"] = 1
            item["box_collider"]["height"] = 60
            item["box_collider"]["width"] = 60
            item["transform"] = {}
            item["transform"]["position"] = [position[0] + 30, position[1] + 30]

        return item
            
    def get_tank_items(self):
        # 地图编辑
        items = []

        items.append(self.get_tank_item("grass", [0, 120]))
        items.append(self.get_tank_item("walls", [0, 180]))
        items.append(self.get_tank_item("walls", [0, 240]))
        items.append(self.get_tank_item("water", [0, 300]))
        items.append(self.get_tank_item("water", [0, 360]))
        items.append(self.get_tank_item("walls", [0, 420]))
        items.append(self.get_tank_item("walls", [0, 480]))
        items.append(self.get_tank_item("grass", [0, 540]))

        items.append(self.get_tank_item("grass", [60, 180]))
        items.append(self.get_tank_item("walls", [60, 240]))
        items.append(self.get_tank_item("water", [60, 300]))
        items.append(self.get_tank_item("walls", [60, 360]))
        items.append(self.get_tank_item("walls", [60, 420]))
        items.append(self.get_tank_item("walls", [60, 480]))
        items.append(self.get_tank_item("water", [60, 540]))
        items.append(self.get_tank_item("grass", [60, 600]))

        items.append(self.get_tank_item("grass", [120, 180]))
        items.append(self.get_tank_item("walls", [120, 240]))
        items.append(self.get_tank_item("water", [120, 300]))
        items.append(self.get_tank_item("walls", [120, 360]))
        items.append(self.get_tank_item("walls", [120, 420]))
        items.append(self.get_tank_item("water", [120, 480]))
        items.append(self.get_tank_item("water", [120, 540]))
        items.append(self.get_tank_item("grass", [120, 600]))

        items.append(self.get_tank_item("grass", [180, 120]))
        items.append(self.get_tank_item("walls", [180, 180]))
        items.append(self.get_tank_item("walls", [180, 240]))
        items.append(self.get_tank_item("walls", [180, 300]))
        items.append(self.get_tank_item("walls", [180, 360]))
        items.append(self.get_tank_item("water", [180, 420]))
        items.append(self.get_tank_item("water", [180, 480]))
        items.append(self.get_tank_item("grass", [180, 540]))

        items.append(self.get_tank_item("walls", [240, 60]))
        items.append(self.get_tank_item("walls", [240, 120]))
        items.append(self.get_tank_item("walls", [240, 180]))
        items.append(self.get_tank_item("iron", [240, 240]))
        items.append(self.get_tank_item("walls", [240, 300]))
        items.append(self.get_tank_item("walls", [240, 360]))
        items.append(self.get_tank_item("walls", [240, 420]))
        items.append(self.get_tank_item("water", [240, 480]))
        items.append(self.get_tank_item("grass", [240, 540]))

        items.append(self.get_tank_item("grass", [300, 120]))
        items.append(self.get_tank_item("walls", [300, 180]))
        items.append(self.get_tank_item("walls", [300, 240]))
        items.append(self.get_tank_item("walls", [300, 300]))
        items.append(self.get_tank_item("walls", [300, 360]))
        items.append(self.get_tank_item("walls", [300, 420]))
        items.append(self.get_tank_item("walls", [300, 480]))
        items.append(self.get_tank_item("grass", [300, 540]))

        items.append(self.get_tank_item("walls", [360, 120]))
        items.append(self.get_tank_item("walls", [360, 180]))
        items.append(self.get_tank_item("iron", [360, 240]))
        items.append(self.get_tank_item("walls", [360, 300]))
        items.append(self.get_tank_item("walls", [360, 360]))
        items.append(self.get_tank_item("walls", [360, 420]))
        items.append(self.get_tank_item("water", [360, 480]))
        items.append(self.get_tank_item("grass", [360, 540]))
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
        items.append(self.get_tank_item("symbol", [360, 728]))

        items.append(self.get_tank_item("grass", [420, 120]))
        items.append(self.get_tank_item("walls", [420, 180]))
        items.append(self.get_tank_item("walls", [420, 240]))
        items.append(self.get_tank_item("walls", [420, 300]))
        items.append(self.get_tank_item("walls", [420, 360]))
        items.append(self.get_tank_item("water", [420, 420]))
        items.append(self.get_tank_item("water", [420, 480]))
        items.append(self.get_tank_item("grass", [420, 540]))

        items.append(self.get_tank_item("grass", [480, 180]))
        items.append(self.get_tank_item("walls", [480, 240]))
        items.append(self.get_tank_item("water", [480, 300]))
        items.append(self.get_tank_item("walls", [480, 360]))
        items.append(self.get_tank_item("walls", [480, 420]))
        items.append(self.get_tank_item("water", [480, 480]))
        items.append(self.get_tank_item("water", [480, 540]))
        items.append(self.get_tank_item("grass", [480, 600]))

        items.append(self.get_tank_item("grass", [540, 180]))
        items.append(self.get_tank_item("walls", [540, 240]))
        items.append(self.get_tank_item("water", [540, 300]))
        items.append(self.get_tank_item("walls", [540, 360]))
        items.append(self.get_tank_item("walls", [540, 420]))
        items.append(self.get_tank_item("walls", [540, 480]))
        items.append(self.get_tank_item("water", [540, 540]))
        items.append(self.get_tank_item("grass", [540, 600]))

        items.append(self.get_tank_item("grass", [600, 120]))
        items.append(self.get_tank_item("walls", [600, 180]))
        items.append(self.get_tank_item("walls", [600, 240]))
        items.append(self.get_tank_item("water", [600, 300]))
        items.append(self.get_tank_item("water", [600, 360]))
        items.append(self.get_tank_item("walls", [600, 420]))
        items.append(self.get_tank_item("walls", [600, 480]))
        items.append(self.get_tank_item("grass", [600, 540]))

        items.append(self.get_tank_item("grass", [660, 180]))
        items.append(self.get_tank_item("grass", [660, 240]))
        items.append(self.get_tank_item("grass", [660, 300]))
        items.append(self.get_tank_item("water", [660, 360]))
        items.append(self.get_tank_item("grass", [660, 420]))
        items.append(self.get_tank_item("water", [660, 480]))
        items.append(self.get_tank_item("water", [660, 540]))
        items.append(self.get_tank_item("grass", [660, 600]))

        items.append(self.get_tank_item("grass", [720, 360]))
        items.append(self.get_tank_item("grass", [720, 420]))
        items.append(self.get_tank_item("water", [720, 480]))
        items.append(self.get_tank_item("grass", [720, 540]))
        return items

    def export_map(self, module: str):
        data = {}
        data["scene_id"] = 0
        data["desc"] = "test"
        data["back_ground"] = ""
        data["window_size"] = (780, 780)
        if module == 'tank':
            data["items"] = self.get_tank_items()

        self.save(module, data)


if __name__ == '__main__':
    t = Test()
    # t.print_all_size("tank")
    t.export_map("tank")
