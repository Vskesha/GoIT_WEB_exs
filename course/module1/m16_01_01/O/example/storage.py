import json
import yaml
import pathlib


class Storage:
    def get_value(self, key):
        raise NotImplementedError


class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f).get(key)


class YAMLStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader).get(key)


class Service:
    def __init__(self, storage: Storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_value(key)


if __name__ == '__main__':

    storage_json = JSONStorage(pathlib.Path() / 'data.json')
    service = Service(storage_json)
    print(service.get('name'))

    storage_yaml = YAMLStorage(pathlib.Path() / 'data.yaml')
    service = Service(storage_yaml)
    print(service.get('name'))
