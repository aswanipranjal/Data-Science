import hlt
import logging
from collections import OrderedDict
import numpy as np
import random
import os

VERSION = 1

HM_ENT_FEATURES = 5
PCT_CHANGE_CHANCE = 30
DESIRED_SHIP_COUNT = 20

game = hlt.Game('Deep-v{}'.format(VERSION))
logging.info('Deep-v{} Start'.format(VERSION))