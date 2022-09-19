#Occasionally it is useful to plot individual points as opposed to providing a general plot.  The motivations for this
#could be to emphasise the difference between the size of the various values by colouring some in one colour and the
#rest in another.

#To scatter a single point, we call upon the "scatter()" method.  We can then pass the single (x,y) values to the point
#of interest to the "scatter()" method to plot these values.  Much like the code found in "mpl_squares.py," the code is
#given by

import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig_1, ax = plt.subplots()
ax.scatter(2,4)

plt.show()

#Just like we did before, let's add a label to each of the axes as well as a title.

import matplotlib.pyplot as plt

plt.style.use("seaborn")
fig_2, ax = plt.subplots()
ax.scatter(2, 4, s=200)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()

#As we know, more often that not we will plotting more than one data point.  Hnece, let us now plot a scatter version of
#the values and their squares.

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("seaborn")
fig_3, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()

#Rather than writing these lists by hand, we can loop the calculations through Python instead by providing a specified
#range of values instead.

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
#As we can see, we have simply made a "for" loop in order to make our lives easier.

plt.style.use("seaborn")
fig_4, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)
#We can also set a limit to the size of the axes' maximum possible values.
ax.axis([0, 1100, 0, 1100000])

plt.show()

#Should one want to change the colour of the points, one can pass "c" through the "scatter()" method along with the name
#of a colour written in the form of a string.  For example, we can produce a figure whose points are red using

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig_5, ax = plt.subplots()
ax.scatter(x_values, y_values, c="red", s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()

#One can also define custom colours using the RGB colour model.  That is, instead of using just one colour, one can
#equate "c" to a number between 0 and 1.  The closer the number is to 0, the darker the colour produced, the closer it
#is to 1, the lighter it is.

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig_6, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0.4, 0, 0), s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()

#One can also use a colourmap in order to indicate how the value of a point based on its colour.

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig_7, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#On line 128, we see that the list named "y_values" is passed through to "c" only for us to then tell "pyplot" to use
#"cmap" argument.

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()

#As pleasant as it is to produce various figures on the spot, it would be even better if we were actually able to save
#these plots automatically to the project file.  This can be achieved by replacing the "plt.show()" with "plt.savefig()"
#in the following way.

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig_8, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.savefig("square_plot.png", bbox_inches="tight")

#The first argument is the filename for the plot's image, the second of which trims the extra whitespace from the plot,
#hence why it says "tight."