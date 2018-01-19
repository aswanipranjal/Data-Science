import hlt
import logging
from collections import OrderedDict

game = hlt.Game('Attacker-v3')
logging.info('Starting Attacker-v3')

while True:
	game_map = game.update_map()
	command_queue = []
	team_ships = game_map.get_me().all_ships()
	for ship in team_ships:
		shipid = ship.id
		if ship.docking_status != ship.DockingStatus.UNDOCKED:
			continue

		entities_by_distance = game_map.nearby_entities_by_distance(ship)
		entities_by_distance = OrderedDict(sorted(entities_by_distance.itens(), key=lambda t: t[0]))
		