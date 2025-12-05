import numpy as np
from world import GridWorld
from bios import Bios

class Simulation:
    def __init__(self, width=128, height=128, initial_bios=100):
        self.world = GridWorld(width, height)
        self.world.add_energy()

        # Add some bios
        for _ in range(initial_bios):
            self.world.bios.append(Bios(x0=np.random.randint(0, width), y0=np.random.randint(0, height)))

        # Statistics history
        self.population_history = []
        self.energy_history = []

    def step(self):
        """
        Updates the grid world for a single time step.
        """
        self.world.add_energy()

        # Bios logic
        for bios in self.world.bios:
            bios.consume_energy()
            bios.move()
            
        # Bios eat
        self.world.bios_eat()

        # Bios reproduce
        for bios in self.world.bios:
            new_bios = bios.reproduce()
            if new_bios is not None:
                self.world.bios.append(new_bios)
        
        # Remove dead bios
        self.world.remove_dead_bios()

        # Decay energy
        self.world.decay_energy()

        # Record statistics
        self.population_history.append(len(self.world.bios))
        self.energy_history.append(np.sum(self.world.grid))

