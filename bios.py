import numpy as np
from world import GridWorld

class Bios:
    def __init__(self, energy: float = 10.0, x0: int = 0, y0: int = 0):
        # Energy level of the bios
        self.energy = energy

        # Initial position
        self.x = x0
        self.y = y0

        # Genetic traits
        self.sustain_energy = 1.0  # energy consumed per step
        self.repr_energy = energy * 2  # energy threshold for reproduction
        self.mutation_chance = 0.1

    def consume_energy(self):
        self.energy -= self.sustain_energy

    def move(self):
        # Move the bios in a random direction
        # randint(low, high) excludes high, so (-1, 2) gives -1, 0, 1
        self.x += np.random.randint(-1, 2)
        self.y += np.random.randint(-1, 2)

    def reproduce(self):
        if self.energy >= self.repr_energy:
            self.energy /= 2
            # New bios with same genetics, possibly mutated
            new_bios = self.copy()
            new_bios.energy = self.energy
            new_bios.mutate()
            return new_bios
        return None
    
    def copy(self):
        new_bios = Bios(energy=self.energy)
        new_bios.sustain_energy = self.sustain_energy
        new_bios.repr_energy = self.repr_energy
        new_bios.mutation_chance = self.mutation_chance
        new_bios.x = self.x
        new_bios.y = self.y
        return new_bios
    
    def mutate(self):
        if np.random.rand() < self.mutation_chance:
            self.sustain_energy += np.random.uniform(-0.2, 0.2)
            self.repr_energy += np.random.uniform(-0.2, 0.2)
            if self.sustain_energy < 1:
                self.sustain_energy = 1
            if self.repr_energy < self.sustain_energy * 2:
                self.repr_energy = self.sustain_energy * 2