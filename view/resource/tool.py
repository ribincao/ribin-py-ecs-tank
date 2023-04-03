import os
import json
import pygame


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
            d = {'mod_id': mod_id, 'mod_name': mod, 'models': []}
            for file in sorted(files):
                file_path = os.path.join(root, file)
                d['models'].append('./view/resource' + file_path[1:])
                self.show_size(file_path)
            mod_id += 1
            gltf.append(d)
    
        # print(gltf)
        self.save(module, gltf)
    
    def show_size(self, path: str):
        if path.endswith('.gif') or path.endswith('.png'):
            img = pygame.image.load(path)
            print(path, img.get_rect())


if __name__ == '__main__':
    gltf = GLTF()
    gltf.export('tank')
