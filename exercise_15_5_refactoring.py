# In order to shorten the method of "fill_walk()," we will write an additional method that will be called "get_step(),"
# in essence allowing us to use it in the "fill_walk()" method, in turn shortening it to an acceptable length.
from random import choice

class RefactoredRandomWalk:
    """A refactored random walk class."""

    def __init__(self, num_points=5000):
        """Initialize the attributes of the refactored random walk."""

        self.num_points = num_points

        # All walks start at the origin (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """A method for obtaining the direction and distance travelled during one step."""
        distance = choice([-1, 1])
        direction = choice([0, 1, 2, 3, 4])
        step = distance * direction
        return step

    def reformed_fill_walk(self):
        """A shortened method for the calculation of all points on the path."""

        while len(self.x_values) < len(num_points):

            x_step = self.get_step()
            y_step = self.get_step()

            # Much like before, we don't count iterations that take us nowhere.
            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    # As can be seen "reformed_fill_walk()" is a more condensed version of its predecessor, "fill_walk()."
