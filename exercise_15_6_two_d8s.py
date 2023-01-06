# For this project, we are going to see what happens when you throw two D8 dice 1000 times.
# I predict that the shape of the distribution of results will resemble the shape of Pascal's triangle in a similar
# manner to the two D6 dice.

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
max_result = die_1.num_sides + die_2.num_sides

# Note to self: remember  ensure that where "roll_num" \= "result."
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Results"}
my_layout = Layout(title="Results of Throwing Two D8 1000 Times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d8_d8.html")
