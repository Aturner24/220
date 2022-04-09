import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def surface_area(self):
        r = self.radius
        return 4 * (r**2) * math.pi
    def volume(self):
        r = self.radius
        return 4/3 * (r**3) *math.pi



