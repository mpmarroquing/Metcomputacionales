#este script deriva la funcion e^(-x^2) en un intervalo -5 a 5
import numpy as np
import math
import matplotlib.pyplot as plt

def funcion(x):
	return (np.e**(-x**2))

def derivada(fn,x,h):
	return (fn(x+h) - fn(x))/h
		
	
	
n_points = 100
h = np.logspace(-0.00000001, 0.00000001, n_points)


x = np.linspace(-1.7,1.7)
for i in range(n_points):
	prime = derivada (funcion,x,h[i])
	print prime

 
plt.plot(x,prime)
plt.show()
