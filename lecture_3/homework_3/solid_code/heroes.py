from abc import ABC, abstractmethod
import random

class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place):
        place.get_antagonist()

    @abstractmethod
    def attack(self):
        pass


class Soldier(SuperHero):
    """боевые искусства и огнестрельное оружие"""
    def a_roundhouse_kick(self):
        print('Bump')

    def a_fire_a_gun(self):
        print('PIU PIU')

    def attack(self):
        cls = type(self)
        attack_funcs = [func for func in dir(cls) if func.startswith('a_')]
        rnd_func = random.choice(attack_funcs)
        cmd = f'self.{rnd_func}()'
        eval(cmd)


class Superman(Soldier):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def ultimate(self):
        self.incinerate_with_lasers()

