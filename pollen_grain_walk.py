import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()

    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(11.5, 6.5), dpi=128)

    ax.scatter(0,0,c = 'green', edgecolors = 'black',s = 3, zorder = 5)

    ax.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red', edgecolors = 'black', s = 3, zorder = 5)

    ax.plot(rw.x_values,rw.y_values,c = 'blue',linewidth= 1)



    ax.set_aspect('equal')

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make Another Walk?(y/n): ")
    if keep_running == 'n':
        break


# plt.savefig('Random_walk.png',bbox_inches = 'tight')