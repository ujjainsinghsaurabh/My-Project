import matplotlib.pyplot as plt

x_values = range(1,1001)
squares = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()

# ax.plot(x_values,squares,color = (0,0.8,0),linewidth = 2)

ax.scatter(x_values,squares,c = squares,cmap = plt.cm.Blues,s = 10)

ax.set_title("Square Numbers",fontsize = 20)
ax.set_xlabel("Value",fontsize = 14)
ax.set_ylabel("Sqaures of Value",fontsize = 14)
ax.tick_params(labelsize = 14)
ax.ticklabel_format(style = 'plain')

ax.axis([0,1100,0,1_100_000])



# plt.show()


