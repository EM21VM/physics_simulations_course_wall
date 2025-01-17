import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.Particle import Particle
from lib.Simulation import Boundary, Simulation
from lib.Wall import Wall
from lib.constants import npdarr, Axes

if __name__ == "__main__":
    print("Testing the Wall class")
    L = 500.0
    simulation = Simulation(
        dt=0.05,
        max_t=50.0,
        sides=[L, L, L],
        boundaries=[Boundary.WALL, Boundary.WALL, Boundary.EMPTY],
    )
    pos = np.array([0, L / 2, 0])
    vel = np.array([10, 0, 0])
    rad = 5
    par = Particle(
        pos=pos + rad,
        vel=vel,
        rad=rad,
        mass=1,
        color="#00FF00",
        opacity=1,
    )
    simulation.add_object(par)
    wal = Wall(
        pos=np.array([L / 2, L, 0]),
        end_pos=np.array([L, 0, 0]),
        color="#FF0000",
        opacity=1,
    )
    simulation.add_object(wal)
    simulation.setup_system()

    fig, ax = plt.subplots()
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    frames_label = ax.annotate(f"frame: 0/{simulation.num_steps:04d}", xy=(10, L - 10))
    overlaps_label = ax.annotate("overlaps: []", (20, 20))
    circle = Circle(
        (par.pos[0], par.pos[1]), par.rad, facecolor=par.color, edgecolor="black", lw=1
    )
    circles = [circle]
    ax.add_patch(circle)
    ax.plot(
        [wal.pos[0], wal.end_pos[0]],
        [wal.pos[1], wal.end_pos[1]],
        [wal.pos[2], wal.end_pos[2]],
    )
    ax.add_patch(
        Rectangle(
            wal.bbox.pts[0],
            wal.bbox.sides[Axes.X],
            wal.bbox.sides[Axes.Y],
            lw=2,
            edgecolor="black",
            facecolor="none",
        )
    )

    def update_sphere_animation(frame):
        for pos, circle in zip(simulation.pos_matrix[frame], circles):
            circle.set_center(pos[:2])
        frames_label.set_text(f"frame: {frame:04d}/{simulation.num_steps:04d}")
        overlaps_label.set_text(f"overlaps:\n[{simulation.AABBs_overlaps[frame]}]")
        return [frames_label]

    simulation.run()
    animation = FuncAnimation(
        fig=fig, func=update_sphere_animation, frames=simulation.num_steps, interval=1
    )
    plt.show()
