from sample import *

# SolarSystem class
class SolarSystem:
    def __init__(self, data):
        self.sun = Sun(data['Name'], data['Diameter'])
        self.planets = [self.create_planet(**planet) for planet in data.get('Planets', [])]

    def create_planet(self, **kwargs):
        planet_kwargs = {
            'name': kwargs.get('Name'),
            'diameter': kwargs.get('Diameter'),
            'circumference': kwargs.get('Circumference'),
            'distance_from_sun': kwargs.get('DistanceFromSun'),
            'orbital_period': kwargs.get('OrbitalPeriod'),
            'moons': [self.create_moon(**moon) for moon in kwargs.get('Moons', [])]
        }

        planet_kwargs = {k: v for k, v in planet_kwargs.items() if v is not None}
        planet = Planet(**planet_kwargs)
        if planet.diameter is None:
            planet.diameter = planet.calculate_diameter_from_circumference()
        elif planet.circumference is None:
            planet.circumference = planet.calculate_circumference_from_diameter()        
        if planet.distance_from_sun is None:
            planet.distance_from_sun = planet.calculate_distance_from_orbit_time()
        elif planet.orbital_period is None:
            planet.orbital_period = planet.calculate_orbit_time_from_distance()        
        return planet
    
    def create_moon(self, **kwargs):
        moon_kwargs = {
            'name': kwargs.get('Name'),
            'diameter': kwargs.get('Diameter'),
            'circumference': kwargs.get('Circumference')
        }
        moon_kwargs = {k: v for k, v in moon_kwargs.items() if v is not None}
        moon = Moon(**moon_kwargs)
        if moon.diameter is None:
            moon.diameter = moon.calculate_diameter_from_circumference()
        elif moon.circumference is None:
            moon.circumference = moon.calculate_circumference_from_diameter()        
        return moon

