import pickledb
from config import config

db = pickledb.load(config['db'], True)
