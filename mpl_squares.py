#Let us begin with a nice and simple line graph.  The graph of choice is the first five squares, from 1 through to 25.
#We begin this task by importing the pyplot module as plt in order for us to not have to write pyplot repeatedly.

import matplotlib.pyplot as plt

#Following the importation of the module, we can then create a list that will be called "squares" that will store the
#first five elements of the set.

squares = [1, 4, 9, 16, 25]

fig_1, ax = plt.subplots()
ax.plot(squares)

plt.show()

#On line 11, we call upon the subplots() function.  This allows one to generate one or more plots in the same figure.
#The "fig" term represents the entire figure/collection of plots that are generated.  The variable "ax" represents a
#single plot in the figure and is the variable that will be most widely used.
#The "plot()" is then used to plot the data provided in a meaningful way.
#On line 14, the function plt.show() opens Matplotlib's viewer and displays the plot.

#Let us now look at the case in which we want to label the axes, provide a title for the graph as well as increase the
#thickness of the plot. In doing so, we need to provide a few additional lines of code.

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig_2, ax = plt.subplots()
ax.plot(squares, linewidth=3)

#We write the following three lines of code in order to provide titles for the horizontal and vertical axes and the
#general plot as a whole.

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)

#I'm not aware of the purpose behind the code that features on line 40.  In the textbook it just says it "styles the
#tick marks."  By tick marks, it means short lines on the axis - now I understand it!
ax.tick_params(axis="both", labelsize=14)

plt.show()

#In spite of how nice this graph may look, it's worth noticing that the "Value Squared" values don't correctly align
#with the values that are being squared.  This is because when you give "plot()" a sequence of numbers, it assumes that
#the first data point corresponds to the x-coordinate's zero value.  This can be remedied by providing the "plot()"
#method with the specified input values.

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig_3, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()

#Let's look at the situation in which we want to produce a more aesthetically pleasing piece of visual aid.  For this to
#be achieved, one must use the "plt.style.use(style_type)" method.  For example, let us set "style_type" = seaborn.

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn")

fig_4, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()

#I opted to test out a few more styles before moving onto plotting individual points.

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn-darkgrid")

fig_5, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("fivethirtyeight")

fig_6, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Squared", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()