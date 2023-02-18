import matplotlib.pyplot as plt
from analyze_files import *

calculate_average()
daten = get_average("Saturday")
print(daten)
plt.plot(daten)
plt.show()
