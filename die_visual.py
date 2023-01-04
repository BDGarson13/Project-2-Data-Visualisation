# Prior to producing a visualisation for the rolling of a die, let us first roll a D6 (DX = X-sided die), print the
# results and check to see if they're reasonable.
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6.
die = Die()

# Let us roll the die 100 times and store in a results list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# In order analyse the results of rolling the die, we must first count the frequency at which each value is rolled.

# The empty list "frequencies" is created in order to store the number of times a certain value is rolled.
frequencies = []
for value in range(1, die.num_sides + 1):
    # Just like it says on the tin, we simply count how many times a particular value appears in our "results" list.
    frequency = results.count(value)
    # We then append this to the "frequencies" list.
    frequencies.append(frequency)

print(frequencies)

# Now that we've accrued the necessary data, we can now go about visualising it by producing a histogram.
# A histogram is a bar chart showing how often certain results occur.
# It is for this reason that lines 3 and 4 were written.

# In order to make a histogram, we need to assign a bar to each of the possible results, storing these in the list that
# we call "x_values."  Because Plotly does not directly accept the "range()" function, we need to convert the range to a
# list explicitly using the "list()" function.
x_values = list(range(1, die.num_sides + 1))
# The class "Bar" represents a dat set that will be formatted like as a bar chart, requiring a list of x and y values.
# Due to the fact that a data set can have multiple elements, it must be stored inside square brackets.
data = [Bar(x=x_values, y=frequencies)]

# Each of the axes have been configured as dictionaries.
x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}
# The "Layout" class returns an object that specifies the layout and configuration of the graph as a whole by setting
# the title of the graph as well as pass the x- and y-axis configuration dictionaries through as well.
my_layout = Layout(title="Results of Rolling a D6 1000 Times", xaxis=x_axis_config, yaxis=y_axis_config)
# Finally, in order to plot the histogram, two arguments are needed for the function.  The first is a dictionary
# containing the data and layout objects while the second is the name that we assign to the file that is made.
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
