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

ship_plans = {}

if os.path.exists('d{}_input.vec'.format(VERSION)):
    os.remove('d{}_input.vec'.format(VERSION))

if os.path.exists('d{}_out.vec'.format(VERSION)):
    os.remove('d{}_out.vec'.format(VERSION))

