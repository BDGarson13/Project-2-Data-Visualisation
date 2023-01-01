# The motivation behind this file is to edit the RandomWalk class by changing the possible values that can be taken as
# the distance travelled along the path.
# We will then be able to see how small changes can lead to very different outcomes.
from random import choice
import matplotlib.pyplot as plt


class ModifiedRandomWalk1:
    """A modified take on the original RandomWalk class."""

    def __init__(self, num_points=5000):
        """Initialise attributes of a walk."""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """A method for calculating all the points in the walk."""

        while len(self.x_values) < self.num_points:

            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# Having modified the distance between various points to be potentially much larger, we can now see the consequences of
# changes in action


while True:

    # "mrw1" being an instance of the class "ModifiedRandomWalk1."
    mrw1 = ModifiedRandomWalk1()
    mrw1.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=125)
    point_numbers = range(mrw1.num_points)

    ax.scatter(mrw1.x_values, mrw1.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=15)
    ax.scatter(0, 0, c="green", edgecolor="none", s=100)
    ax.scatter(mrw1.x_values[-1], mrw1.y_values[-1], c="red", edgecolor="none", s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another iteration? (y/n): ")
    if keep_running == "n":
        break

# The second modified class will now have a direction with a double factor.


class ModifiedRandomWalk2:
    """A modified take on the original RandomWalk class."""

    def __init__(self, num_points=5000):
        """Initialise attributes of a walk."""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """A method for calculating all the points in the walk."""

        while len(self.x_values) < self.num_points:

            x_direction = choice([-2, 2])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-2, 2])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# Much like before, we will see how much of a difference is made with this change to the conditions.


while True:

    mrw2 = ModifiedRandomWalk2()
    mrw2.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=125)
    point_numbers = range(mrw2.num_points)

    ax.scatter(mrw2.x_values, mrw2.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=15)
    ax.scatter(0, 0, c="green", edgecolor="none", s=100)
    ax.scatter(mrw2.x_values[-1], mrw2.y_values[-1], edgecolor="none", s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another iteration? (y/n): ")
    if keep_running == "n":
        break
