import matplotlib.pyplot as plt


value_start = int(input("Input the starting point for Values: "))
value_end = int(input("Input the Ending point for Values: "))
try:
    skip_value = int(input("Interval for Values and their Cubes: "))
    if skip_value == 0:
        raise ValueError("Interval cannot be zero.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()


values = range(value_start,value_end+1,skip_value)

cube_values = [x**3 for x in values]

fig,ax = plt.subplots()

ax.scatter(values,cube_values, c = cube_values,cmap = plt.cm.Blues,s = 10)

ax.set_title("Cube of Values",fontsize = 20)
ax.set_xlabel("Values",fontsize = 14)
ax.set_ylabel("Cube of Values", fontsize = 14)
ax.tick_params(labelsize = 14)
ax.ticklabel_format(style = 'plain')

ax.axis([0,value_end,0,cube_values[-1]])

plt.show()



