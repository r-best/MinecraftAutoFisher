import os
import json
from .screengrabber import grab

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "config.json")

coords = grab()
data = dict()
data['tesseract_path'] = ""
try:
    with open(CONFIG_FILE, 'r') as fp:
        data = json.load(fp)
except FileNotFoundError:
    print("Config file '{}' does not exist, creating a new one".format(CONFIG_FILE))
except json.decoder.JSONDecodeError:
    print("Error parsing config file '{}', creating a new one".format(CONFIG_FILE))
finally:
    with open(CONFIG_FILE, 'w+') as fp:
        data['screengrab_coords'] = coords
        data['tesseract_path'] = data['tesseract_path']
        json.dump(data, fp, indent=4, sort_keys=True)
