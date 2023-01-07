# We can now see whether the same distribution shape will differ, if at all, when considering three dice being rolled as
# opposed to just two.

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_config = {"title": "Result", "dtick": 1}
y_config = {"title": "Frequency of Results"}
# Must remember that the "Layout()" class has arguments as its inputs, not key-value pairs!
my_layout = Layout(title="Result of Throwing Three D6 Dice 1000 Times", xaxis=x_config, yaxis=y_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d6_d6.html")
