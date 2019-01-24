import os
import sys
import json
import getopt
from .fisher import start
from .screengrabber import grab

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "config.json")

# Read command line args
try:
    opts, args = getopt.getopt(sys.argv[1:], "s", ["levdist=", "tesspath=", "new-bbox"])
except getopt.GetoptError as e:
    print(e)
    print("python -m mc-autofisher [--levdist x] [--tesspath x] [-s|--new-bbox] [...]")
    sys.exit(2)

params = {
    "tesspath": -1,
    "error_margin": -1,
    "bbox": -1
}
# Process command line args and assign parameter values
for opt, arg in opts:
    if opt == "--tesspath":
        tesspath = arg
    if opt == "--levdist":
        try: error_margin = int(arg)
        except ValueError:
            print("ERROR: Allowed Levenshtein distance must be a whole number")
    if opt in ("-s", "--new-bbox"):
        bbox = grab()
        try:
            with open(CONFIG_FILE, 'r') as fp:
                temp = json.load(fp)
            with open(CONFIG_FILE, 'w+') as fp:
                temp['bbox'] = bbox
                json.dump(temp, fp, indent=4, sort_keys=True)
        except:
            print("ERROR: Unable to save new bbox to config file")

# If any of the parameters have not been set on command line,
# load them from config file
if -1 in params.values():
    try:
        with open(CONFIG_FILE, 'r') as fp:
            config = json.load(fp)
    except FileNotFoundError:
        print(f"ERROR: Config file {CONFIG_FILE} does not exist")
        exit()
    except json.decoder.JSONDecodeError:
        print(f"ERROR: Config file {CONFIG_FILE} is malformed, if you changed it manually please make sure it is valid JSON")
        exit()

    try:
        if params["tesspath"] == -1:
            params["tesspath"] = config["tesseract_path"]
        if params["error_margin"] == -1:
            params["error_margin"] = config["allowed_levdist"]
        if params["bbox"] == -1:
            # If 4 or more tagless args were provided, accept them as the bbox
            # Else get the bbox from the config file
            if len(args) >= 4:
                try: bbox = [int(x) for x in args[:4]]
                except ValueError:
                    print("One of the provided bounding box values was not a number")
            else:
                params["bbox"] = config["bbox"]
    except KeyError:
        print(f"ERROR: Please check that the config file {CONFIG_FILE} contains all required values")

# Start the fisher
start(params["bbox"],
    allowed_error=params["error_margin"],
    tesspath=params["tesspath"])
