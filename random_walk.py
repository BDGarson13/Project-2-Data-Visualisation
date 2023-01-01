# A random walk is a path that has no clear direction but is instead determined by a series of random decisions, each
# one being left entirely to chance.  An example of something that might do this is a confused ant.

# We must first create a RandomWalk class which will be responsible fo making the random decisions about which direction
# the walk should take.
# The class needs three attributes: one variable to store the x- and y- coordinate values of each point in the walk and
# two lists to store the x- and y- coordinate values of each point in the walk.
# As a result, only two methods for the random walk class will be required, these being the "__init__()" method and the
# "fill_walk()" method.
# By starting with the former, we have

# This is required in order for us to use the "choice" function in order decide which move to make each time a step is
# taken.
from random import choice


class RandomWalk:
    """A class that generates random walks."""

    # In order for an interesting enough pattern to be generated at a reasonable speed, the number of points is set to
    # 5000.
    def __init__(self, num_points=5000):
        """Initialise attributes of a walk."""
        self.num_points = num_points

        # Setting all walks to start at (0,0).
        # As well as this, we make two lists to hold the x- and y- values.
        self.x_values = [0]
        self.y_values = [0]

    # In order to fill our walk with points and determine the direction of each step , we will write the following:
    def fill_walk(self):
        """A method for calculating all the points in the walk."""

        # The while loop below tells us that we can only continue to execute any of the following code while the number
        # of points doesn't exceed 5000.
        while len(self.x_values) < self.num_points:

            # By using the "choice" function below, we are returned with either the value of 1 or -1.
            x_direction = choice([1, -1])
            # The second use of the function below allows us to be returned with any integer between 0 and 4.
            x_distance = choice([0, 1, 2, 3, 4])
            # By multiplying the distance by our direction factor, we obtain a term that tells us how far in one of two
            # directions we move.  For example, if "x-direction=+1" then we know that we travel to the right and left
            # for the case in which we're returned with -1.
            x_step = x_direction * x_distance

            # We will now do the exact same but this time for the y-axis, yielding us with
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # By ensuring that we don't count any instances where we remain stationary, we'll write the condition
            if x_step == 0 and y_step == 0:
                continue

            # In order to calculate the new positions, we add the x- and y- steps to the last elements of the
            # "self.x_values" and "self.y_values" lists, i.e. the -1th elements.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # These newly-calculated are then appended to the lists of both the x and y values.
            self.x_values.append(x)
            self.y_values.append(y)
