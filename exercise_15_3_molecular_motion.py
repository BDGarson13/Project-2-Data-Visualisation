# The goal of this exercise is to simulate the path of a pollen grain on the surface of a drop of water by opting for a
# plotting of the points as opposed to the standard scatter plot that was used for the random walk.
# The "while" loop method shall be retained in order for multiple

# By importing the class RandomWalk, we can reduce the amount of effort required to produce a random path.
from random_walk import RandomWalk
import matplotlib.pyplot as plt

# We'll write "mm" for molecular motion.
while True:

    mm = RandomWalk()
    mm.fill_walk()

# To now plot the path of the molecule, we write the following

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(mm.num_points)
    ax.plot(mm.x_values, mm.y_values, linewidth=1, zorder=1)

    # In order to make the path easier to follow, we can get rid of the axes as well as emphasise the start and end of
    # the path much like what was done in the case of the random walk plot.
    # The "zorder" argument is used such that we can prioritise the presence of the points with higher "zorder" values.

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.scatter(0, 0, c="green", s=100, edgecolors="none", zorder=2)
    ax.scatter(mm.x_values[-1], mm.y_values[-1], c="red", s=100, edgecolors="none", zorder=2)

    plt.show()

    keep_running = input("Make another simulation? (y/n): ")
    if keep_running == "n":
        break
