import numpy as np
import matplotlib.pyplot as plt

DatosMarzo = np.loadtxt("DatosMarzo.txt")

Datos = np.loadtxt("GRF_vs_EQ.txt")

grfM = DatosMarzo[:,0]
eqM = DatosMarzo[:,1]

grf = Datos[:,0]
eq = Datos[:,1]


plt.scatter(grf, eq, c="black",label='Para todos los meses',s=15)
plt.scatter(grfM, eqM, c="green",label='Para Marzo',s=150)
plt.xlabel("Glacier&&RockFall")
plt.ylabel("Largest Earthquake")
plt.legend(loc="upper left")
plt.show()