#EXERCISE 15-1

#Here is how one can plot the first five cubes.

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.style.use("seaborn")

fig_1, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()

#I will now plot the first 5000 cubes by utilising the "for" loop technique that was seen in "scatter_squares.py".

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")

fig_2, ax = plt.subplots()
ax.scatter(x_values, y_values, c="cyan", s=10)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()

#EXERCISE 15-2

#Let us now apply a colourmap to the cube plot that was produced above.  While the exercise doesn't call for us to save
#the plot as a "png" file, I'll do so regardless!

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")

fig_3, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=10)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.savefig("cube_plot.png", bbox_inches="tight")

#A test to determine whether the new directory actually works.
