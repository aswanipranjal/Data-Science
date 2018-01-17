import os
import sys
import random

description = """
---- Newton's Cradle ----
A screensaver version of Newton's Cradle with an interactive mode
/s run in fullscreen screensaver mode
/p display a preview of the screensaver using a window handler
/i interactive mode
"""

if len(sys.argv) < 2:
	print(description)
	sys.exit()

is_interactive = False
display_flags = 0
if sys.argv[1] == "/p": # preview mode
	os.environ['SDL_VIDEODRIVER'] = 'windib'
	os.environ['SDL_WINDOWID'] = sys.argv[2]
	display_size = (100, 100)
	is_interactive = False

import pygame
from pygame.locals import *
from pygame.color import *

if sys.argv[1] == "/s": # fullscreen screensaver mode
	display_size = (0, 0)
	is_interactive = False
	display_flags = display_flags | FULLSCREEN # FULLSCREEN | DOUBLEBUF | HWSURFACE
elif sys.argv[1] == "/i": # interactive
	display_size = (600, 600)
	is_interactive = True

