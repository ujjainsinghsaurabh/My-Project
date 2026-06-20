import plotly.express as px

from die import Die

die = Die()

results =[]

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

frequencies = []

poss_results = range(1,die.num_sides+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)
title = "Results of Rolling one D6 1,000 Times"
labels = {'x':'Result','y':'Frequency of result'}
fig = px.bar(x = poss_results, y = frequencies,title = title, labels = labels)
# fig = px.scatter(x = poss_results, y = frequencies)
# fig = px.line(x = poss_results, y = frequencies)
fig.show() 