# (b) Given the following definition of the geometric Point class, complete the distance
# method that takes one other point and returns the distance between them:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        distance_squared = (self.x - p.x) ** 2 + ((self.y - p.y) ** 2)
        distance = distance_squared ** (1 / 2)
        return distance


p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1.distance(p2))
