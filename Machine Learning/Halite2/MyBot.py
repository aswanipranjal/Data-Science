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

while True:
    game_map = game.update_map()
    command_queue = []

    team_ships = game_map.get_me().all_ships()
    all_ships = game_map._all_ships()
    enemy_ships = [ship for ship in game_map._all_ships() if ship not in team_ships]

    my_ship_count = len(team_ships)
    enemy_ship_count = len(enemy_ships)
    all_ship_count = len(all_ships)

    my_id = game_map.get_me().id
    empty_planet_sizes = {}
    our_planet_sizes = {}
    enemy_planet_sizes = {}

    for p in game.all_planets():
        radius = p.radius
        if not p.is_owned():
            empty_planet_sizes[radius] = p
        elif p.owner.id == game_map.get_me.id:
            our_planet_sizes[radius] = p
        elif p.owner.id != game_map.get_me.id:
            enemy_planet_sizes[radius] = p

    hm_our_planets = len(our_planet_sizes)
    hm_empty_planets = len(empty_planet_sizes)
    hm_enemy_planets = len(enemy_planet_sizes)

    empty_planet_keys = sorted([k for k in empty_planet_sizes])[::-1]
    our_planet_keys = sorted([k for k in our_planet_sizes])[::-1]
    enemy_planet_keys = sorted([k for k  in enemy_planet_sizes])[::-1]

    for ship in game_map.get_me().all_ships():
        try:
            if ship.docking_status != ship.DockingStatus.UNDOCKED:
                continue

            shipid = ship.id
            change = False
            if random.randint(1, 100) <= PCT_CHANGE_CHANCE:
                change = True

            entities_by_distance = game_map.nearby_entities_by_distance(ship)
            entities_by_distance = OrderedDict(sorted(entities_by_distance.items(), key=lambda t: t[0]))

            closest_empty_planets = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and not entities_by_distance[distance][0].is_owned()]
            closest_empty_planet_distances = [distance for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and not entities_by_distance[distance][0].is_owned()]

            closest_my_planets = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and entities_by_distance[distance][0].is_owned() and (entities_by_distance[distance][0].owner.id == game_map.get_me().id)]
            closest_my_planet_distances = [distance for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and entities_by_distance[distance][0].is_owned() and (entities_by_distance[distance][0].owner.id == game_map.get_me().id)]

            closest_enemy_planets = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and entities_by_distance[distance][0] not in closest_my_planets and entities_by_distance[distance][0] not in closest_empty_planets]
            closest_enemy_planet_distances = [distance for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Planet) and entities_by_distance[distance][0] not in closest_my_planets and entities_by_distance[distance][0] not in closest_empty_planets]

            closest_team_ships = [entities_by_distance[distance][0] for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Ship) and entities_by_distance[distance][0] in team_ships]
            closest_team_ship_distances = [distance for distance in entities_by_distance if isinstance(entities_by_distance[distance][0], hlt.entity.Ship) and entities_by_distance[distance][0] in team_ships]

            