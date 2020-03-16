import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv


def generate(data_names, data_values):
    

    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
    mpl.rcParams.update({'font.size': 10})

    plt.title('Кол-во заказов по дням')

    ax = plt.axes()
    ax.yaxis.grid(True, zorder = 1)

    xs = range(len(data_names))

    plt.bar([x + 0.05 for x in xs], [ d * 0.9 for d in data_values],
            width = 0.2, color = 'blue', alpha = 0.7, zorder = 2)
    plt.xticks(xs, data_names)

    fig.autofmt_xdate(rotation = 25)

    plt.legend(loc='upper right')
    fig.savefig('stat.png')