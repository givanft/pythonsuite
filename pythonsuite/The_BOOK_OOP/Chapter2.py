#####################################################################################

import math
class Point:
    """
     Represents a point in two-dimensional geometric coordinates
     >>> p_0 = Point()
     >>> p_1 = Point(3, 4)
     >>> p_0.calculate_distance(p_1)
     5.0
     """
    def __init__(
        self, 
        x: float = 0.0, 
        y: float = 0.0) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calc_dist(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

p1 = Point(3, 5)
p2 = Point()

p1.reset()
p2.move(5, 0)

print(p2.calc_dist(p1))

p1.move(3, 4)

print(p1.calc_dist(p2))

print(p1.calc_dist(p1))

#####################################################################################

#class Point:
#    def reset(self) -> None:
#        self.x = 0
#        self.y = 0
#p = Point()
#p.reset()
#print(p.x, p.y)