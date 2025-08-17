import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Earth's axial tilt in radians
iota = 23.5 * np.pi / 180

def R_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), np.sin(theta)],
        [0, -np.sin(theta), np.cos(theta)]
    ])

def R_y(theta):
    return np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])

def R_z(theta):
    return np.array([
        [np.cos(theta), np.sin(theta), 0],
        [-np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def daylight(latitude, longitude, day_of_the_year):
    # Calculate beta based on the day of the year
    beta = (2 * np.pi * day_of_the_year/ 365) 
    print(beta)
    # Calculate sidereal time as angle
    sigma = longitude*np.pi / 180 + 2 * np.pi + beta 

    # @ performs the matrix multiplication
    e_x = np.array([1, 0, 0])
    
    e_sun = e_x @ (R_z(beta) @ R_x(-iota)) 

    e_perp = e_x @ (R_y(np.radians(latitude)) @ R_z(sigma)) 

    # Dot product
    return (e_perp @ e_sun.T).T

def plot_daylight(day_of_year, time):
    latitudes = np.linspace(-90, 90, 180)
    longitudes = np.linspace(-180, 180, 360)
    lat_grid, lon_grid = np.meshgrid(latitudes, longitudes) # np.meshgrid() converts the 1D vectors representing the axes into 2D arrays

    # Compute daylight values
    values = np.vectorize(daylight)(lat_grid, lon_grid, day_of_year)
    
    # np.vectorize() converts the daylight function into a vectorized function that can take NumPy arrays as input arguments and return a NumPy array of outputs. 
    
    plt.figure(figsize=(12, 6))
    plt.contourf(lon_grid, lat_grid, values, levels=np.linspace(-1, 1, 21), cmap='coolwarm', norm=colors.Normalize(-1,1))
    plt.colorbar(label='Sunlight Projection')
    plt.title(f'Daylight Map on Day {day_of_year} at Time {time}:00')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()

# Example
plot_daylight(170, 6)  
