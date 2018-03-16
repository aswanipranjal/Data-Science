# author: ad71
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

from functools import partial

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import astar_search, EightPuzzle
import utils

