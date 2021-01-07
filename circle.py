# https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/

import math

class Circle():
    def __init__(self, radius=1):
        self.radius = radius

    def __str__(self):
        return f"Circle({self.radius})"

    def __repr__(self):
        return f"Circle({self.radius})"

    def radius(self, r):
        self.radius = r

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pow(self.radius, 2) * math.pi

