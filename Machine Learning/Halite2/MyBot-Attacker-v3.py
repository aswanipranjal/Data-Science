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
		closest_enemy_ships =   [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Ship) and entities_by_distance[distance][0] not in team_ships]
		closest_empty_planet_distances = [distance for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and not entities_by_distance[distance][0].is_owned()]
		closest_enemy_ship_distances =   [distance for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Ship) and entities_by_distance[distance][0] not in team_ships]

		# If there are empty planets nearby
		if len(closest_empty_planets) > 0:
			# If there are enemy ships nearby
			if len(closest_enemy_ships) > 0:
				# If closest empty planet is twice the distance of the closest enemy ship, we would rather attack the enemy ship as our chances of reaching the planet are small
				# Let's test if this hyper-aggressive approach works well
				if (closest_empty_planet_distances[0] >= (2 * closest_enemy_ship_distances[0])):
					target_ship = closest_enemy_ships[0]
					navigate_command = ship.navigate(ship.closest_point_to(target_ship), game_map, speed=int(hlt.constants.MAX_SPEED), ignore_ships=False)
					if navigate_command:
						command_queue.append(navigate_command)

				else:
					target_planet = closest_empty_planets[0]
					if ship.can_dock(target_planet):
						command_queue.append(ship.dock(target_planet))
					else:
						navigate_command = ship.navigate(ship.closest_point_to(target_planet), game_map, speed=int(hlt.constants.MAX_SPEED), ignore_ships=False)
						if navigate_command:
							command_queue.append(navigate_command)

			# There are no enemy ships nearby
			else:
				target_planet = closest_empty_planets[0]
				if ship.can_dock(target_planet):
					command_queue.append(ship.dock(target_planet))
				else:
					navigate_command = ship.navigate(ship.closest_point_to(target_planet), game_map, speed=int(hlt.constants.MAX_SPEED), ignore_ships=False)
					if navigate_command:
						command_queue.append(navigate_command)

		# There are no empty planets nearby but there are enemy ships
		elif len(closest_enemy_ships) > 0:
			target_ship = closest_enemy_ships[0]
			navigate_command = ship.navigate(ship.closest_point_to(target_ship), game_map, speed=int(hlt.constants.MAX_SPEED), ignore_ships=False)
			if navigate_command:
				command_queue.append(navigate_command)

        # There are neither empty planets nor enemy ships nearby
    	else:
    		pass

    game.send_command_queue(command_queue)