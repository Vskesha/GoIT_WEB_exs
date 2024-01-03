import configparser
from pymongo import MongoClient
from pathlib import Path
from django.conf import settings


filename = Path(settings.BASE_DIR) / 'config.ini'
config = configparser.ConfigParser()
config.read(filename)

user = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')

client = MongoClient(f"mongodb+srv://{user}:{password}@clustervs1.fmxueib.mongodb.net/?retryWrites=true&w=majority")

db = client['web16']
