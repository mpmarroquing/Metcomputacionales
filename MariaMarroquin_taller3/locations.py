import random
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import hist, show

contenido = np.loadtxt("locationsY.txt")




plt.hist(contenido[:,0],bins=15,color="gray")
plt.title("Latitud")
plt.show()

plt.hist(contenido[:,1],bins=15)
plt.title("Longitud")
plt.show()

print np.argmax((hist(contenido[:,0],bins=15))[:,0])
print np.argmax((hist(contenido[:,1],bins=15))[:,1])