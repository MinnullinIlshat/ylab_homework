from abc import ABC, abstractmethod
import random

class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place):
        place.get_antagonist()

    # Проблема: Для каждого супергероя реализованы все методы обращения с оружием.
    # Несоблюден: Принцип разделения интерфейса
    # По SOLID: Создать классы-миксины для каждого оружия
    # Когда возникнут трудности? Попробуйте запретить Чаку норрису пользоваться лазерами из глаз!

    @abstractmethod
    def attack(self):
        pass

    # Проблема: У разных супергероев разные суперспособности
    # Несоблюден: Принцип открытости/закрытости
    # По SOLID: Каждого супергероя реализовать как наследника SuperHero и вместо изменения базового класса переопределять нужные методы
    # Когда возникнут трудности? Когда в вашем коде поселится вся команда Мстителей
    @abstractmethod
    def ultimate(self):
        pass


class Fighter(SuperHero):
    """боевые искусства"""
    def a_roundhouse_kick(self):
        print('Bump')

class Shooter(SuperHero):
    """огнестрельное оружие"""
    def a_fire_a_gun(self):
        print('PIU PIU')

class Superman(Fighter, Shooter):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def attack(self):
        attack_funcs = [func for func in dir(Superman) if func.startswith('a_')]
        rnd_func = random.choice(attack_funcs)
        cmd = f'self.{rnd_func}()'
        eval(cmd)

    def ultimate(self):
        self.incinerate_with_lasers()

Superman().attack()
