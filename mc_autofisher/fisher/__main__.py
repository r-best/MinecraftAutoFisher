import sys
import json
from .fisher import start

CONFIG_FILE = "config.json"
if len(sys.argv) > 1:
    CONFIG_FILE = sys.argv[0]

try:
    with open(CONFIG_FILE, 'r') as fp:
        data = json.load(fp)
    start(tuple(data['screengrab_coords']), data['tesseract_path'])
except FileNotFoundError:
    print("ERROR: Config file '{}' does not exist, please run the screengrabber".format(CONFIG_FILE))
    exit()
except json.decoder.JSONDecodeError:
    print("ERROR: Config file '{}' is malformed, if you changed it manually please make sure it is valid JSON".format(CONFIG_FILE))
    exit()
except Exception:
    raise
