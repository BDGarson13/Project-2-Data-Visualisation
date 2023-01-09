# Now we want to investigate the distribution of results generated when we multiply the results of the individual dice
# rolls as opposed to add.

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

# I am now converting all "for" loops to the list comprehension format as can be seen below.
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Results"}
my_layout = Layout(title="Results of Multiplying Two D6 Dice", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6_x_d6.html")

# As can be seen from the distribution, there is no longer a pyramid-type distribution observed.
