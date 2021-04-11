import json


class FileLoader:
    @staticmethod
    def load(file):
        file = open('data/%s' % file, 'r')
        return json.loads(file.read())

    @staticmethod
    def save(file, data):
        file = open('data/%s' % file, 'w')
        file.write(json.dumps(data))
        file.close()
