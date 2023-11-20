from storage import *


class Service:

    def __init__(self, storage: Storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_value(key)


if __name__ == '__main__':

    service = Service(JSONStorage('data.json'))
    print(service.get('name'), service.get('age'))

    service = Service(YAMLStorage('data.yaml'))
    print(service.get('name'), service.get('age'))
