import random
import numpy as np
import math
import matplotlib.pylab as plt
from matplotlib.pylab import hist, show

contenido = np.loadtxt("magnitudesY.txt")

plt.hist(contenido,bins=5,color="green")
plt.title("Magnitudes")
plt.show()




dist_sup = ( 1 - np.cumsum(contenido))
	
	
plt.plot (dist_sup, np.log(dist_sup))
plt.show()