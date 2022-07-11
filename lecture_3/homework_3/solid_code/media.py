from abc import ABC, abstractmethod 

class MassMedia(ABC):

    @abstractmethod
    def create_news(self):
        pass 


class TvNews(MassMedia):

    def create_news(self, place, hero):
        place_name = getattr(place, 'name', 'place')
        print(f'{hero.name} saved the {place_name}!')

class HoloMedia(MassMedia):
    """всегаллактическая коммуникационная сеть"""

    def create_news(self, place, hero):
        place_name = getattr(place, 'coordinates', 'place')
        place_name = ', '.join(place_name) if not isinstance(place_name, str) else place_name 
        print(f'{hero.name} saved the {place_name}')
