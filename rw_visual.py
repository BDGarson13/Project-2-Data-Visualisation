# In order to plot all the points that were calculated in the "random_walk.py" file, we can import from that file the
# class of the same name as follows.

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Should we want to continue making new walks while the program is active, we introduce a while loop.
while True:

    # We can make a random walk by writing
    rw = RandomWalk()
    rw.fill_walk()

    # By calling the method "fill_walk()," we produce all the x- and y- values necessary for the plot to be made.
    # Much like what was done in the previous plotting instances, having already imported matplotlib, followed by
    # choosing a style as well as an appropriate dot size.

    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    # Should we wish to continue producing random walks, we simply input "y" when prompted.
    # If the opposite is the case, we will answer the question with "n."

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# We can also customise the plot in such a way as to indicate the order of the points in the walk.
# One way in which this can be achieved is by changing the colour of the points as the iteration continues to be made.
# Given how small the dots are in size, we can remove the dark outline, leaving just the variation of blue.

# Just like before, we write our standard "while" loop
while True:

    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    # By running the "point_numbers" through the "c" argument.  Due to the points being plotted in order, it follows
    # that the list just contains the numbers from 0 to 4999.
    point_numbers = range(rw.num_points)
    # As mentioned before, by setting 'edgecolors="none,"' the dark outline is removed
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# In order to better emphasise the starting and end points of the path, we can provide two additional lines of code to
# highlight these stages.

while True:

    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
    # The starting point is green and enlarged, while the end point is red and still noticeably bigger than the rest.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# In spite of axes being essential features to discern the values of the variables concerned, they can be considered
# distractions in this case given our interest in illustrating the direction of the path taken as opposed to the extent
# of that path.

while True:

    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # We can remove the axes by using the "get_xaxis()" and "get_yaxis()" methods and setting their visibilities to
    # "False," enabling us to remove the axes from our final plot.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# We can also increase the number of points on the scatter plot by inserting the new number of points in the brackets.

while True:

    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=1)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# Yet another thing that can be done is to ensure that the visualisation fits nicely onto the screen.  This can be done
# via the employment of the "figsize" argument given below.

while True:

    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=1)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
