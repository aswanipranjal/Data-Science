import hlt
import logging
from collections import OrderedDict

game = hlt.Game('Attacker-v1')
logging.info('Starting Attacker')

while True:
    game_map = game.update_map()
    command_queue = []

    for ship in game_map.get_me().all_ships():
        shipid = ship.id
        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            