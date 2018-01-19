import hlt
import logging
from collections import OrderedDict

game = hlt.Game('Attacker-v2')
logging.info('Starting Attacker-v2')

while True:
	game_map = game.update_map()
	command_queue = []
	team_ships = game_map.get_me().all_ships()
	team_ships_extra = []
	if len(team_ships) > 20:
		team_ships_main = team_ships[:20]
		team_ships_extra = team_ships[20:]
	for ship in team_ships_main:
		shipid = ship.id
		if ship.docking_status != ship.DockingStatus.UNDOCKED:
			continue

			