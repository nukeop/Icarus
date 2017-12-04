from tinydb import TinyDB
from config import config

db = TinyDB(config['db'])
