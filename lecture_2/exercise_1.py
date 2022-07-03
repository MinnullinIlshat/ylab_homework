import math
from itertools import permutations

class Point:
    """точка в системе координат"""
    def __init__(self, x=0, y=0, address=None):
        self.address = address if address else 'Точка маршрута'
        self.x = x
        self.y = y

    def get_distance(self, other):
        """возвращает float - расстояние между точками"""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def __str__(self):
        return f'{self.address}(x={self.x}, y={self.y})'

class Route:
    """ маршрут """
    def __init__(self, start=None, points=None):
        self.points = [] 
        self._get_points(points)
        self.start = start if start else Point(0, 0)
        self.routes = [] # cписок кортежей с точками
        self._get_routes()

    def get_shortest_route(self):
        """возвращает самый короткий маршрут"""
        r, d = None, 99999
        for route in self.routes:
            dist = self._get_route_distance(route)
            if dist < d:
                r, d = route, dist
        return r, d 

    def _get_points(self, points):
        """points - последовательность кортежей с координатами"""
        for point in points:
            x, y, address = point
            self.points.append(Point(x, y, address))

    def _get_route(self, points):
        """принимает кортеж с последовательностью точек, добавляет начало и конец"""
        route = (self.start,) + points + (self.start,)
        return route

    def _get_route_distance(self, points):
        """принимает последовательность точек и возвращает длину маршрута"""
        distance = 0.0
        for i in range(len(points) - 1):
            distance += points[i].get_distance(points[i+1])
        return distance

    def _get_routes(self):
        """добавляет все возможные маршруты в список self.routes"""
        for points in permutations(self.points, len(self.points)):
            route = self._get_route(points)
            self.routes.append(route)


if __name__ == '__main__':
    start = Point(0, 2, 'Почтовое отделение          ')
    points = (
        (2, 5, 'Ул. Грибоедова, 104/25      '),
        (5, 2, 'Ул. Бейкер стрит, 221б      '),
        (6, 6, 'Ул. Большая Садовая, 302-бис'),
        (8, 3, 'Вечнозеленая Аллея, 742     '))
    route = Route(start, points)
    shortest, length = route.get_shortest_route()

    print(f"Начало маршрута: {shortest[0]}\n")
    current_dist = 0
    for i in range(1, len(shortest)):
        current_dist += shortest[i].get_distance(shortest[i-1])
        print(f'{i} {shortest[i]}. Пройдено: {current_dist}')
    print(f'\nПолная длина маршрута: {current_dist}')
