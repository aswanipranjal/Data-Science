import hlt
import logging
from collections import OrderedDict

game = hlt.Game('Attacker-v3')
logging.info('Starting Attacker-v3')

while True:
	game_map = game.update_map()
	command_queue = []
	team_ships = game_map.get_me().all_ships()
	