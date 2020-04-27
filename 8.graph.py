#%pylab inline
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D as ax


x = np.arange(0, 10, 0.1)
y = np.sin(x)

fig, ax= plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, y, marker="o", color="r", linestyle='None')

ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.legend(["y = x**2"])

plt.title('Puntos')
plt.show()

fig.savefig("grafica.png")
