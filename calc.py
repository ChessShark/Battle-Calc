from copy import copy
from battle_library import *

infantry = Land_Unit(INF, 1, 1, 2, None, True)
tank = Land_Unit(TNK, 3, 3, 5, None, None)
artillery = Land_Unit(ART, 2, 2, 4, True, None)

attacking_army = [infantry, tank]
defending_army = [tank, infantry]
initial_attacking_army = copy(attacking_army)
initial_defending_army = copy(defending_army)

armies = Armies(attacking_army, defending_army)
initial_armies = Armies(initial_attacking_army, initial_defending_army)

attacker_count = 0
defender_count = 0
draw_count = 0
tuv = 0
total_runs = 100000

pre_battle_print(attacking_army, defending_army)
for simulation_count in range(total_runs):
    battle(armies)
    if len(armies.attacking_army) > len(armies.defending_army):
        attacker_count += 1
    elif len(armies.defending_army) > len(armies.attacking_army):
        defender_count += 1
    else:
        draw_count += 1
    tuv_difference = tuv_calculator(initial_armies, armies)
    tuv += tuv_difference
    armies.attacking_army = copy(initial_attacking_army)
    armies.defending_army = copy(initial_defending_army)
print(
    f"\nAttacker Win Rate: {round(attacker_count / total_runs * 100, 2)}%"
    f"\nDefender Win Rate: {round(defender_count / total_runs * 100, 2)}%"
    f"\nDraw: {round(draw_count / total_runs * 100, 2)}%"
    f"\nAverage Tuv difference = {round(tuv / total_runs, 2)}")