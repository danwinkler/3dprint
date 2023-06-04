import math
import random
from dataclasses import dataclass

import numpy as np
from lib.helper import *
from solid import *
from solid.utils import *

parts = []

width = 920
height = 550


print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
