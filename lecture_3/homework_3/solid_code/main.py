from typing import Union
from heroes import Superman, SuperHero
from places import Kostroma, Tokyo
from media import TvNews, MassMedia


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], massmedia: MassMedia):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    massmedia.create_news(place, hero)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TvNews())
    print('-' * 20)
    save_the_place(SuperHero('Chack Norris', False), Tokyo(), TvNews())
