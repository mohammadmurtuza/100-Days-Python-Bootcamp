import math
from SolarSystem import sun as solar_system_data

# CelestialObject class
class CelestialObject:
    def __init__(self, name, diameter=None, circumference=None):
        self.name = name
        self.diameter = diameter
        self.circumference = circumference
        self.volume = self.calculate_volume()

    def calculate_diameter_from_circumference(self):
        if self.circumference is not None and self.diameter is None:
            self.diameter = self.circumference / math.pi
        return self.diameter

    def calculate_circumference_from_diameter(self):
        if self.diameter is not None and self.circumference is None:
            self.circumference = self.diameter * math.pi
        return self.circumference

    def calculate_volume(self):
        if self.diameter is not None:
            radius = self.diameter / 2
            return (4/3) * math.pi * (radius ** 3)
        else:
            return 0

# Sun class
class Sun(CelestialObject):
    def __init__(self, name, diameter):
        super().__init__(name, diameter)
        self.planets = []
        self.circumference = self.calculate_circumference_from_diameter()

    def sum_volume_of_planets(self):
        return sum(planet.volume for planet in self.planets)

# Planet class
class Planet(CelestialObject):
    def __init__(self, name, diameter=None, circumference=None, distance_from_sun=None, orbital_period=None, moons=None):
        super().__init__(name, diameter, circumference)
        self.diameter = diameter
        self.circumference = circumference
        self.distance_from_sun = distance_from_sun
        self.orbital_period = orbital_period
        self.moons = [moon if isinstance(moon, Moon) else Moon(**moon) for moon in (moons or [])]

    def calculate_orbit_time_from_distance(self):
        if self.distance_from_sun is not None and self.orbital_period is None:
            self.orbital_period = math.sqrt(self.distance_from_sun ** 3)
        return self.orbital_period

    def calculate_distance_from_orbit_time(self):
        if self.orbital_period is not None and self.distance_from_sun is None:
            self.distance_from_sun = self.orbital_period ** (2/3)
        return self.distance_from_sun

# Moon class
class Moon(CelestialObject):
    pass

