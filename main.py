import PySimpleGUI as sg
from analyzer.plot_files import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg



# Create the form and show it without the plot
layout = [
    [sg.Text("Auslastung")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Ok")],
]
fig = get_Plot("Saturday")

# window of the application
window = sg.Window(
    "RWTH GYM Aulastung",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

# add the pyplot to the window
draw_figure(window["-CANVAS-"].TKCanvas, fig)
event, values = window.read()
window.close()

