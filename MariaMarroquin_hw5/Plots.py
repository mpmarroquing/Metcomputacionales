import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("RadialVelocities.dat")
r=datos[:,0]
v=datos[:,1]

plt.scatter(r,v)
plt.xlabel("Radio(kpc)")
plt.ylabel("Velocidad(km/s)")
plt.savefig("datos.pdf")