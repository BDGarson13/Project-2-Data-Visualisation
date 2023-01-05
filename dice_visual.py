# By rolling two dice, larger numbers and a different distribution of results can be observed.
# We will create two D6 dice, write code that simulates them being rolled and their results recorded.

# Much like before, we import the two classes and one function that we need to produce a histogram.
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# We will now create two instances of the "Die" class.

die_1 = Die()
die_2 = Die()

# We will now make some rolls and store the subsequent results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# The results now undergo analysis in an almost identical manner to before.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Now for the visualisation of the results, we write
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# We create the same dictionary as before, but this time with an additional "dtick" key.
# The value assigned to this is a measure of how far apart the tick marks are from each other on the x-axis.
x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of Throwing Two D6 1000 Times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d6.html")
