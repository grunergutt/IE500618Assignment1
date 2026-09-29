import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def setup_plot_style(x=12, y=6, grid=True):
    plt.figure(figsize=(x, y))
    plt.grid(grid)
