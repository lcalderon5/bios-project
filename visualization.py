import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from simulation import Simulation

class Visualizer:
    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        
        # Initialize the image with the starting grid
        self.im = self.ax.imshow(
            self.simulation.world.grid,
            cmap='inferno', 
            vmin=0, 
            vmax=self.simulation.world.max_energy, 
            interpolation='nearest'
        )
        
        plt.colorbar(self.im, label='Energy Level')
        
        # Initialize scatter plot for bios
        self.scat = self.ax.scatter([], [], c='green', s=10, label='Bios')
        self.ax.legend(loc='upper right')
        
        self.title = self.ax.set_title(f'Grid World Simulation: Step 0 - Population: {len(self.simulation.world.bios)}')

    def update(self, frame):
        # Update the simulation state
        self.simulation.step()
        
        # Update the image data
        self.im.set_data(self.simulation.world.grid)
        
        # Update bios positions
        if self.simulation.world.bios:
            # Extract x and y coordinates
            x_data = [bio.x for bio in self.simulation.world.bios]
            y_data = [bio.y for bio in self.simulation.world.bios]
            self.scat.set_offsets(np.c_[x_data, y_data])
        else:
            self.scat.set_offsets(np.empty((0, 2)))

        self.title.set_text(f'Grid World Simulation: Step {frame+1} - Population: {len(self.simulation.world.bios)}')
        return self.im, self.scat, self.title

    def start(self, steps=100, interval=50):
        ani = animation.FuncAnimation(
            self.fig, 
            self.update, 
            frames=steps, 
            interval=interval, 
            blit=False,
            repeat=False
        )
        plt.show()

