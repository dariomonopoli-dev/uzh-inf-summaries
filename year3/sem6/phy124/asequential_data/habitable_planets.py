T_sun = 5800  # (in Kelvin)

planets_with_similar_daylight = []

fyle = open("exoplanet.csv", "r")
lines = fyle.readlines()

header = lines[0].strip().split(",")  # Extract the column names
star_radius_idx = header.index("star_radius")
semi_major_axis_idx = header.index("semi_major_axis")
star_teff_idx = header.index("star_teff")

for line in lines[1:]:  # Skip the header
    columns = line.strip().split(",")

    try:
        star_radius = float(columns[star_radius_idx])
        star_teff = float(columns[star_teff_idx])
        semi_major_axis = float(columns[semi_major_axis_idx])

        daylight_strength = (
            (star_radius**2) * ((star_teff / T_sun) ** 4) * (semi_major_axis**-2)
        )

        if 0.5 <= daylight_strength <= 2:  # factor of 2
            planet_name = columns[0]
            planets_with_similar_daylight.append(
                planet_name + ": Daylight strength: " + str(round(daylight_strength, 3))
            )
    except ValueError:  # In case of missing (NA values)
        continue

for planet in planets_with_similar_daylight:
    print(planet)
