# a) Given the following definition of the geometric Point class:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # complete the distance function that takes two Points as input arguments and returns
    # the distance between them:
    def distance(p1, p2):
        x = 0
        y = 0
        if p1.x > p2.x:
            x = p1.x - p2.x
        else:
            x = p2.x - p1.x
        if p1.y > p2.y:
            y = p1.y - p2.y
        else:
            y = p2.y - p1.y
        distance_squared = ((x * x) + (y * y))
        distance = distance_squared ** (1 / 2)
        return distance
p1 = Point(1, 2)
p2 = Point(4, 6)

