from random import randint

INF = "Infantry"
TNK = "Tank"
ART = "Artillery"
CAV = "Cavalry"
STR = "Stormtruppen"


class Land_Unit:
    def __init__(self, name, attack, defense, tuv, supporting, supportable):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.tuv = int(tuv)
        self.supporting = supporting
        self.supportable = supportable

    def Attack(self):
        roll_die = randint(1, 6)
        if roll_die <= self.attack:
            return True

    def Defense(self):
        roll_die = randint(1, 6)
        if roll_die <= self.defense:
            return True


class Armies:
    def __init__(self, attacking_army, defending_army):
        self.attacking_army = attacking_army
        self.defending_army = defending_army


def contains(army, unit_name):
    for unit in army:
        if unit.name == unit_name:
            return True


def revert_unit_values(army):
    for supported_unit in army:
        if supported_unit.name == INF:
            supported_unit.attack == 1
        if supported_unit.name == CAV:
            supported_unit.attack == 1
        if supported_unit.name == STR:
            supported_unit.attack == 2


def remove_from_army(army, unit_name):
    for unit in army:
        if unit.name == unit_name:
            army.remove(unit)


def remove_attacking_units(hits, army):
    for hit in range(hits):
        if contains(army, INF):
            remove_from_army(army, INF)
            continue
        if contains(army, ART):
            remove_from_army(army, ART)
            continue
        if contains(army, TNK):
            remove_from_army(army, TNK)
            continue
    return army


def support_function(attacking_army):
    for unit in attacking_army:
        if unit.supporting:
            for other_unit in attacking_army:
                if other_unit.supportable:
                    unit.attack += 1
                    break


def tuv_calculator(initial_armies, armies):
    initial_attacking_tuv = 0
    initial_defending_tuv = 0
    remaining_attackers_tuv = 0
    remaining_defenders_tuv = 0
    for unit in initial_armies.attacking_army:
        initial_attacking_tuv += unit.tuv
    for unit in initial_armies.defending_army:
        initial_defending_tuv += unit.tuv
    for unit in armies.attacking_army:
        remaining_attackers_tuv += unit.tuv
    for unit in armies.defending_army:
        remaining_defenders_tuv += unit.tuv
    total_attack_loss = initial_attacking_tuv - remaining_attackers_tuv
    total_defense_loss = initial_defending_tuv - remaining_defenders_tuv
    tuv_difference = total_defense_loss - total_attack_loss
    return tuv_difference


def attack_roll(army):
    support_function(army)
    hits = 0
    for each_unit in army:
        if each_unit.Attack():
            hits += 1
    return hits


def defense_roll(army):
    hits = 0
    for each_unit in army:
        if each_unit.Defense():
            hits += 1
    return hits


def battle(armies):
    while len(armies.attacking_army) > 0 and len(armies.defending_army) > 0:
        attack_hits = attack_roll(armies.attacking_army)
        defense_hits = defense_roll(armies.defending_army)
        armies.attacking_army = remove_attacking_units(defense_hits, armies.attacking_army)
        armies.defending_army = remove_attacking_units(attack_hits, armies.defending_army)
        revert_unit_values(armies.attacking_army)


def pre_battle_print(attacking_army, defending_army):
    print("Attackers:", end=" ")
    for unit in attacking_army:
        print(f"{unit.name}", end=" ")
    print("\nDefenders:", end=" ")
    for unit in defending_army:
        print(f"{unit.name}", end=" ")
