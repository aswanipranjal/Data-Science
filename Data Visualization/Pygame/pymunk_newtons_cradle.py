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