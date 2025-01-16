import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import Axes3D

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    )
from lib.Particle import Particle
from lib.Simulation import Boundary, Simulation
from lib.Wall import Wall

if __name__ == "__main__":
    print("Testing the Wall class")
    L = 500.0
    simulation = Simulation(
        dt=0.05,
        max_t=50.0,
        sides=[L, L, L],
        boundaries=[Boundary.WALL, Boundary.WALL, Boundary.WALL],
    )
    par = Particle([0, 1, 0], [0, 1, 0], 1, 1, "#FF000", 1)
    simulation.add_object(par)
    wal = Wall([3, 0, 0], [3, 3, 0])
    simulation.add_object(wal)
    simulation.setup_system()
    simulation.put_particles_on_grid(
        Ns=np.array([10, 10, 1]), dL=np.array([20.0, 20.0, 20.0])
    )

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_zlim(0, L)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    frame_label = ax.annotate(f"frame: 0/{simulation.num_steps:04d}", xy=(10, L - 10))
    plt.show()
