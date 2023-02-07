from _config_section import ConfigSection
from pathlib import Path, PureWindowsPath
import os
from movement.constant import data_dir

REAL_PATH = data_dir

data = ConfigSection("data")
data.dir = PureWindowsPath("%s/%s" % (REAL_PATH, "data"))

data.movement = ConfigSection("movement data")
data.movement.dir = PureWindowsPath("%s/%s" % (REAL_PATH, "data/movement"))

data.shots = ConfigSection("shot information data")
data.shots.dir = PureWindowsPath("%s/%s" % (REAL_PATH, "data/shots"))
