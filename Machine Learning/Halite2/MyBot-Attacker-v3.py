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

		closest_empty_planets = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and not entities_by_distance[distance][0].is_owned()]
		closest_enemy_ships = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Ship) and entities_by_distance[distance][0] not in team_ships]
		