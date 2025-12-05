from simulation import Simulation
from visualization import Visualizer
import matplotlib.pyplot as plt
import random

def main():
    # Initialize the simulation
    sim = Simulation(width=64, height=64, initial_bios=1)
    
    # Initialize the visualizer with the simulation instance
    viz = Visualizer(sim)
    
    # Start the visualization
    viz.start(steps=2000, interval=50)

    # Plot results after simulation
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Population Plot
    ax1.plot(sim.population_history, color='green', label='Population')
    ax1.set_ylabel('Population')
    ax1.set_title('Simulation Statistics')
    ax1.legend()
    ax1.grid(True)
    
    # Energy Plot
    ax2.plot(sim.energy_history, color='orange', label='Total Grid Energy')
    ax2.set_ylabel('Energy')
    ax2.set_xlabel('Step')
    ax2.legend()
    ax2.grid(True)
    
    # Analyze Bios Genetics
    if sim.world.bios:
        print("\n--- Random Bios Analysis ---")
        sample_size = min(5, len(sim.world.bios))
        sample_bios = random.sample(sim.world.bios, sample_size)
        for i, bio in enumerate(sample_bios):
            print(f"Bio {i+1}:")
            print(f"  Energy: {bio.energy:.2f}")
            print(f"  Sustain Energy: {bio.sustain_energy:.4f}")
            print(f"  Reproduction Energy: {bio.repr_energy:.2f}")
            print(f"  Mutation Chance: {bio.mutation_chance:.2f}")
            print("-" * 20)
    else:
        print("\nNo bios survived the simulation.")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
