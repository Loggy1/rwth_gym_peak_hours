from math import trunc
from matplotlib.artist import Artist
import matplotlib.pyplot as plt
from analyzer.analyze_files import *
import matplotlib.figure
import numpy as np


calculate_average()

def on_plot_hover(event, plot, fig):
        try:
            for curve in plot.get_lines():
                if curve.contains(event)[0]:
                    fig.gca().texts[0].set_text(str(int(event.ydata)))
                    fig.gca().texts[0].set_position((event.xdata - 0.5, event.ydata))
                    fig.canvas.draw_idle()
        except:
            pass

# function that returns the plot
def get_Plot(week_day):
    fig = matplotlib.figure.Figure(figsize=(10, 5), dpi=100)
    fig.suptitle(week_day)

    daten = get_average(week_day)
    hours = np.arange(10, 23)
    plot = fig.add_subplot(111)
    plot.plot(hours, daten)

    # Display the x and y coords of the curve at the point that was hovered over
    fig.gca().text(10, 140, 'Graph berühren für mehr Informationen', fontsize=12)
    fig.canvas.mpl_connect('motion_notify_event', lambda event: on_plot_hover(event, plot, fig))

    # set max of y axis to 150 and mark all above 60 as red
    fig.gca().set_ylim([0, 150])
    fig.gca().fill_between(hours, 60, 150, color='red', alpha=0.2)
    
    return fig

