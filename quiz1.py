import numpy as np
import matplotlib.pyplot as plt

#calcular la velocidad en funcion del tiempo

datos = np.loadtxt("Piedra.dat")
posicion= datos[:,1]
tiempo=datos[:,0]

print len(tiempo)

def velocidad(x,t):
	v=[10]
	deltat=0.01
	for i in range(0, 100):
		dev=(x[i+1]-x[i])/(deltat)
		v.append(dev)
	return v
	

vel=velocidad(posicion,tiempo)
print vel

plt.plot(vel,tiempo)
plt.xlabel("velocidad")
plt.ylabel("tiempo")
plt.show()