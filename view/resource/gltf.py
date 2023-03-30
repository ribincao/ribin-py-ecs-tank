import os
from common.logger import logger
from common.data_util import data_util

class GLTF(object):

    def __init__(self):
        pass

    def export(self, module: str):
        mod_id = 0
        for root, dirs, files in os.walk('./' + module):
            if dirs:
                continue
            mod = root.split('/')[-1]
            for file in files:
                file_path = os.path.join(root, file)
                print(mod_id, '-', mod, '-', file_path)
                mod_id += 1

    def load_models(self, module: str, mod_name: str):
        gltf_data = data_util.load_from_json(f'./view/resource/{module}/gltf.json')
        if not gltf_data:
            return []
        logger.debug(f"gltf_load {gltf_data}")
        for data in gltf_data:
            _mod_name = data.get('mod_name', '')
            if _mod_name != mod_name:
                continue
            return data.get('models', [])
        return []


if __name__ == '__main__':
    gltf = GLTF()
    gltf.export('tank')

