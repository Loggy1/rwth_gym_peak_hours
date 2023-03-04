import datetime
import PySimpleGUI as sg
from analyzer.plot_files import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

current_day = datetime.datetime.today()

# Function to draw the plot in the window
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Replaces the plot with the plot for the previous or next day
def replace_fig_agg(fig_agg, window, prev):
    fig_agg.get_tk_widget().forget()
    plt.close('all')
    global current_day 
    if prev:
        current_day -= datetime.timedelta(days=1)
    else:
        current_day += datetime.timedelta(days=1)
    fig = get_Plot(current_day.strftime("%A"))
    return draw_figure(window["-CANVAS-"].TKCanvas, fig)


# Layout of the application
layout = [
    [sg.Text("Auslastung")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Previous")],
    [sg.Button("Next")],
    
]

# window of the application
window = sg.Window(
    "RWTH GYM Aulastung",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

# Add the pyplot to the window
fig = get_Plot(current_day.strftime("%A"))
fig_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)

# event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Previous':
            fig_agg = replace_fig_agg(fig_agg, window, True)
    elif event == 'Next':
            fig_agg = replace_fig_agg(fig_agg, window, False)
window.close()
