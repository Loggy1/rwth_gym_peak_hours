import matplotlib.pyplot as plt
from analyzer.analyze_files import *
import matplotlib.figure
import numpy as np


calculate_average()

# function that returns the plot
def get_Plot(week_day):
    fig = matplotlib.figure.Figure(figsize=(10, 5), dpi=100)
    fig.suptitle(week_day)

    daten = get_average(week_day)
    hours = np.arange(10, 23)
    fig.add_subplot(111).plot(hours, daten)
    
    # set max of y axis to 150 and mark all above 60 as red
    fig.gca().set_ylim([0, 150])
    fig.gca().fill_between(hours, 60, 150, color='red', alpha=0.2)
    return fig

