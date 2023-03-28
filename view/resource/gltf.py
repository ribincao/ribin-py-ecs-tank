import os
from common.logger import logger
from common.data_util import data_util

class GLTF(object):

    def __init__(self):
        pass

    def export(self, module: str):
        for root, dirs, files in os.walk('./' + module):
            if dirs:
                continue
            mod_id = root.split('/')[-1]
            for file in files:
                file_path = os.path.join(root, file)
                print(mod_id, '-', file_path)

    def load_models(self, module: str, mod_id: int):
        gltf_data = data_util.load_from_json(f'./view/resource/{module}/gltf.json')
        logger.info(f"gltf_load {gltf_data}")
        for data in gltf_data:
            _mod_id = data.get('mod_id', -1)
            if _mod_id != mod_id:
                continue
            return data.get('models', [])
        return []


if __name__ == '__main__':
    gltf = GLTF()
    gltf.export('tank')

