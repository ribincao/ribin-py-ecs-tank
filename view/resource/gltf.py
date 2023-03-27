import os

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



if __name__ == '__main__':
    gltf = GLTF()
    gltf.export('tank')

