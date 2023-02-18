import matplotlib.pyplot as plt
from analyzer.analyze_files import *
import matplotlib.figure
import numpy as np


calculate_average()

# function that returns the plot
def get_Plot(week_day):
    fig = matplotlib.figure.Figure(figsize=(10, 5), dpi=100)
    daten = get_average(week_day)
    # Fill array with numbers between 10 and 22
    hours = np.arange(10, 23)
    print(daten)
    fig.add_subplot(111).plot(hours, daten)
    return fig

