import json
from ..levels.level0 import run_level0
from ..levels.level1 import run_level1
from ..levels.level2 import run_level2
from ..levels.level3 import run_level3
from ..levels.level4 import run_level4

# this entire file is fucked. we need some way to get the current level index and make it go up if the user is in the specific ending area.
# maybe we make this out of user control, use time.sleep to delay for a second and then move them up as soon as they enter the finale room for that level.

# fix importing with os.path and sys.path to 
levelInfoDir = "levels\\levelInformation.json"

levelIndex = {
    0: run_level0,
    1: run_level1,
    2: run_level2, 
    3: run_level3,
    4: "unavaliable"
}

def cmd_up():
    with open(levelInfoDir, "r") as f:
        d = json.load(f)
    currentLevel = d['currentLevel']
    nextLevel = int(currentLevel) + 1
    levelIndex[nextLevel]
    tempJson = {"currentLevel": nextLevel}
    with open(levelInfoDir, "w") as f: 
        json.dump(tempJson, f)

if __name__ == "__main__":
    cmd_up()