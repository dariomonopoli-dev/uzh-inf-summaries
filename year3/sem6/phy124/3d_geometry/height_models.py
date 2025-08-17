import numpy as np
import matplotlib.pyplot as plt


terrain = np.loadtxt('data/terrain.xyz', skiprows=1)  
surface = np.loadtxt('data/surface.xyz', skiprows=1)


# Extract coordinates
x_terrain, y_terrain, z_terrain = terrain[:,0], terrain[:,1], terrain[:,2]
x_surface, y_surface, z_surface = surface[:,0], surface[:,1], surface[:,2]


dimension = int(np.sqrt(len(z_terrain)))
z_terrain_grid = z_terrain.reshape((dimension, dimension))
z_surface_grid = z_surface.reshape((dimension, dimension))


plt.figure(figsize=(10, 10))
plt.contourf(x_terrain.reshape((dimension, dimension)), y_terrain.reshape((dimension, dimension)), z_surface_grid - z_terrain_grid, levels=100, cmap='viridis')
plt.colorbar()
plt.title('Height of Vegetation and Buildings Above the Terrain')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.axis('equal') 
plt.show()