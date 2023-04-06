import os
import json
import pygame
from typing import Tuple


class GLTF(object):
    
    def __init__(self):
        pass

    def save(self, module, data):
        with open(f"./{module}/gltf.json", "w") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def export(self, module: str):
        gltf = []
        mod_id = 0
        for root, dirs, files in os.walk('./' + module):
            if dirs:
                continue
            mod = root.split('/')[-1]
            model = {'model_id': mod_id, 'model_name': mod, 'models': []}
            index = 0
            for file in sorted(files):
                d = {}
                file_path = os.path.join(root, file)
                d["index"] = index
                d["model"] = './view/resource' + file_path[1:]
                d["size"] = self.get_size(file_path) 
                model["models"].append(d)
                index += 1
            mod_id += 1
            gltf.append(model)
    
        # print(gltf)
        self.save(module, gltf)

    def get_size(self, path: str) -> Tuple[int, int]:
        if path.endswith('.gif') or path.endswith('.png'):
            img = pygame.image.load(path)
            rect = img.get_rect()
            return rect.width, rect.height
        return 0, 0
    
    def show_size(self, path: str):
        if path.endswith('.gif') or path.endswith('.png'):
            img = pygame.image.load(path)
            print(path, img.get_rect())

    def load_models(self, module: str, mod_name: str):
        with open(f'./view/resource/{module}/gltf.json/{module}/gltf.json', "r", encoding="utf-8") as f:
            gltf_data = json.load(f)
            if not gltf_data:
                return []
            for data in gltf_data:
                _mod_name = data.get('model_name', '')
                if _mod_name != mod_name:
                    continue
                return data.get('models', [])
            return []

if __name__ == '__main__':
    gltf = GLTF()
    gltf.export('tank')
