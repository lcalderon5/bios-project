import numpy as np

class GridWorld:
    def __init__(self, width=64, height=64, max_energy=10):

        self.width = width
        self.height = height
        self.max_energy = max_energy # Max energy PER CELL
        self.grid = np.zeros((height, width))

        self.bios = []

    def print_stats(self):
        print(f"Grid World Size: {self.width}x{self.height}")
        total_cells = self.width * self.height
        print(f"Total Cells: {total_cells}")
        total_energy = np.sum(self.grid)
        print(f"Total Energy in Grid: {total_energy}")

    def add_energy(self):
        energy = np.random.uniform(low=0, high=1, size=(self.height, self.width))
        self.grid += energy

        # Ensure energy does not exceed a maximum value
        self.grid[self.grid > self.max_energy] = self.max_energy

    def decay_energy(self, decay=1):
        decay = np.random.uniform(low=0, high=decay, size=(self.height, self.width))
        self.grid -= decay
        # Ensure energy does not go below zero
        self.grid[self.grid < 0] = 0

    def remove_dead_bios(self):
        self.bios = [bios for bios in self.bios if bios.energy > 0]

    def bios_eat(self):
        # Group bios by position
        bios_by_pos = {}
        for bio in self.bios:
            # Ensure bio is within bounds before letting it eat
            # (Though movement should ideally handle this, we check here to be safe)
            if 0 <= bio.x < self.width and 0 <= bio.y < self.height:
                pos = (bio.x, bio.y)
                if pos not in bios_by_pos:
                    bios_by_pos[pos] = []
                bios_by_pos[pos].append(bio)
        
        # Distribute energy
        if self.grid.ndim != 2:
            print(f"ERROR: Grid is not 2D! Shape: {self.grid.shape}")

        for (x, y), bios_in_cell in bios_by_pos.items():
            try:
                available_energy = self.grid[y, x]
                if available_energy > 0:
                    # Share energy equally
                    share = available_energy / len(bios_in_cell)
                    for bio in bios_in_cell:
                        bio.energy += share
                    
                    # Remove consumed energy from grid
                    self.grid[y, x] = 0
            except IndexError as e:
                print(f"IndexError at ({x}, {y}) with grid shape {self.grid.shape}: {e}")
                raise e

if __name__ == "__main__":
    world = GridWorld()
    world.print_stats()
