#1.1 Leer los archivos de datos (MarsOrbit.dat y EarthOrbit.dat) y guardar las variables relevantes en arrays. colm 2x,3y,4z,1t

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import linalg

#variables para la Tierra
t1=[]
x1=[]
y1=[]
z1=[]

t1 = np.genfromtxt("EarthOrbit.dat",usecols=(0),delimiter=" ")
x1 = np.genfromtxt("EarthOrbit.dat",usecols=(1),delimiter=" ")
y1 = np.genfromtxt("EarthOrbit.dat",usecols=(2),delimiter=" ")
z1 = np.genfromtxt("EarthOrbit.dat",usecols=(3),delimiter=" ")
 
#variables para Marte

t2=[]
x2=[]
y2=[]
z2=[]

t2 = np.genfromtxt("MarsOrbit.dat",usecols=(0),delimiter=" ")
x2 = np.genfromtxt("MarsOrbit.dat",usecols=(1),delimiter=" ")
y2 = np.genfromtxt("MarsOrbit.dat",usecols=(2),delimiter=" ")
z2 = np.genfromtxt("MarsOrbit.dat",usecols=(3),delimiter=" ")

#1.2 graficas de las orbitas

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, z1, c="black",label='Orbita Tierra')
ax.plot(x2, y2, z2, c="blue",label='Orbita Marte')
ax.set_xlabel("posicion x")
ax.set_ylabel("posicion y")
ax.set_zlabel("posicion z")
ax.legend(loc="upper left")

#1.3
plt.savefig("Orbitas.pdf")

#1.4 a partir de las posiciones calcular la masa del sol


#MASA CON LAS POSICIONES DE LA TIERRA
dev_a=[]
dev_b=[]
dev_c=[]
def v(x):
	dev_a=[]
	dev_b=[]
	dev_c=[]
	delta_t= (2.738*10**-3)*31536000
	for i in range (1, 363):
		a=(x1[i+1]-2*x1[i]+x1[i-1])/((delta_t)**2)
		dev_a.append(a)
		b=(y1[i+1]-2*y1[i]+y1[i-1])/((delta_t)**2)
		dev_b.append(b)
		c=(z1[i+1]-2*z1[i]+z1[i-1])/((delta_t)**2)
		dev_c.append(c)
	return dev_a[x],dev_b[x],dev_c[x]	


x=[]
z=[]
def ac(v):
	x=[]
	z=[]
	for i in range (0, 362):
		c=((np.linalg.norm(v(i))*(1.49*10**11)**3)/(6.67*10**-11))
		x.append(c)
	z=np.array(x)
	return np.mean(z)

print "La masa del Sol obtenida a partir de las posiciones de la Tierra es", ac(v), "kg"


#MASA CON MARTE
dev_a1=[]
dev_b1=[]
dev_c1=[]
def v1(x):
	dev_a1=[]
	dev_b1=[]
	dev_c1=[]
	delta_t= (2.738*10**-3)*31536000
	for i in range (1, 363):
		a1=(x2[i+1]-2*x2[i]+x2[i-1])/((delta_t)**2)
		dev_a1.append(a1)
		b1=(y2[i+1]-2*y2[i]+y2[i-1])/((delta_t)**2)
		dev_b1.append(b1)
		c1=(z2[i+1]-2*z2[i]+z2[i-1])/((delta_t)**2)
		dev_c1.append(c1)
	return dev_a1[x],dev_b1[x],dev_c1[x]	

y=[]
k=[]
def ac1(v):
	y=[]
	k=[]
	for i in range (0, 362):
		c=((np.linalg.norm(v1(i))*(1.38**2)*(1.49*10**11)**3)/(6.67*10**-11))
		y.append(c)
	k=np.array(y)
	return np.mean(k)

print "La masa del Sol obtenida a partir de las posiciones de Marte es", ac1(v1), "kg"