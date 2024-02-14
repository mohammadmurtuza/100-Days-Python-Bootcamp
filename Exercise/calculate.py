from Lisy1 import *


# Main function
def main():
    solar_system = SolarSystem(solar_system_data)
    print(f"Sun: {solar_system.sun.name}")
    print(f"Diameter: {solar_system.sun.diameter:,} km")
    print(f"Circumference: {solar_system.sun.circumference:,.0f} km")
    sun_volume = solar_system.sun.volume
    total_volume = 0  
    
    print("...")
    
    for planet in solar_system.planets:
        print(f"Planet: {planet.name}")
        print(f"  Distance from sun: {planet.distance_from_sun} AU")
        print(f"  Orbital period: {planet.orbital_period} years")
        print(f"  Diameter: {planet.diameter:,} km" )
        print(f"  Circumference: {planet.circumference:,.0f} km")
        planet_volume = planet.volume  
        total_volume += planet_volume 
        for moon in planet.moons:
            print(f"    Moon: {moon.name}")
            print(f"      Diameter: {moon.diameter:,} km")
            print(f"      Circumference: {moon.circumference:,.0f} km")
            moon_volume = moon.volume
            total_volume += moon_volume  
        print("...")
    
    print(f"Sun Volume: {sun_volume:,.0f} cubic km")
    print(f"Total Volume of Planets and Moons: {total_volume:,.0f} cubic km")
    
    can_fit_in_sun = total_volume > sun_volume
    print(f"All the planets’ volumes added together could fit in the Sun: {can_fit_in_sun}")

if __name__ == "__main__":
    main()