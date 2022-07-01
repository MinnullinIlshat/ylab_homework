import math
from itertools import permutations

class Point:
    """точка в системе координат"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_distance(self, other):
        """возвращает float - расстояние между точками"""
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

class Route:
    """ маршрут """
    def __init__(self, start=None, points=None):
        self.points = self._get_points(points) if points else []
        self.start = start if start else Point(0, 0)
        self.routes = [] # cписок кортежей с точками
        self._get_routes()

    def get_shortest_route(self):
        d = {}
        for route in self.routes:
            d[route] = self._get_route_distance(route)
        

    def _get_points(self, points):
        """points - последовательность кортежей с координатами"""
        for point in points:
            x, y = point
            self.points.append(Point(x, y))

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