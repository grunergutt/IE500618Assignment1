import matplotlib.pyplot as plt
import pandas as pd

from config import PATH_AMESHOUSING


def plot_histogram(df, column, bins=100):
    plt.grid(True)
    df = df[df.columns[column]]
    plt.hist(df, bins=bins)
    plt.show()
