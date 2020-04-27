#%pylab inline
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D as ax

x = np.arange(-50, 50, 0.1)
y = np.sin(x)
plt.plot(x,y)

plt.title('Puntos')
plt.show()
