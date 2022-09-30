import pandas as pd
import matplotlib.pyplot as plt
from time import time
from random import randint


def file_bmi(filename):
    df = pd.read_csv(filename)
    height = list(df['Height'])
    weight = list(df['Weight'])
    bmi = [703 * (y / x ** 2) for x, y in zip(height, weight)]
    df['BMI'] = bmi
    new_filename = filename[:-4] + '_bmi' + filename[-4:]
    df.to_csv(new_filename, index=False)


def plot_signals(filename):
    df = pd.read_csv(filename)
    columns = list(df.columns)[1:]
    plt.plot(df['x'], df[columns[0]], label=columns[0], color=(0, .50, 0), marker="o", linestyle='--', linewidth='2')
    plt.plot(df['x'], df[columns[1]], label=columns[1], color=(0, .75, .75), marker="+", linestyle=':', linewidth='2')
    plt.plot(df['x'], df[columns[2]], label=columns[2], color=(1.0, .50, 0), marker="D", linestyle='-.', linewidth='2')
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('amplitude')
    new_filename = filename[:-4] + '_plot.png'
    plt.title(new_filename)
    plt.savefig(new_filename)


def grade_histogram(filename):
    df = pd.read_csv(filename)
    bins = [*range(0, 101, 5)]
    bad_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    columns = list(df.columns)
    x = list(df[columns[0]])
    print('here is x: ', x)

    plt.hist(x, bins=bad_bins, facecolor=(0, 1, 1), edgecolor=(0, 0, 0), hatch='/')
    plt.xlabel('Grade')
    plt.ylabel('Count')
    plt.margins(x=0)
    new_filename = filename[:-4] + '_hist.png'
    plt.title(new_filename)
    plt.savefig(new_filename)


def time_it(data_structure, trials, uncontained_value):
    start_time = time()
    for x in range(trials):
        uncontained_value in data_structure

    end_time = time()
    total_time = end_time - start_time
    return total_time / trials


grade_histogram('fakegrades.csv')
