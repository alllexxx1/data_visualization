import matplotlib.pyplot as plt
from data_visualization.random_walk import RandomWalk

while True:

    random_walk = RandomWalk(50000)
    random_walk.fill_walk()
    point_numbers = range(random_walk.num_points)

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.scatter(random_walk.x_values, random_walk.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolor='none', s=2)
    ax.scatter(0, 0, c='green', edgecolor='none', s=50)
    ax.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red',
               edgecolor='none', s=50)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another random walk? (y/n): ')
    if keep_running == 'n':
        break
    elif keep_running == 'y':
        continue
