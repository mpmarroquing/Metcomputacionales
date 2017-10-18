import math
import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
	return 1/(math.sqrt(1+np.cos(x)*np.sin(x)))

lower_limit=0
upper_limit=3.3						#a y b limites de integracion
N=6									#puntos separados una distancia h en el area de integracion

#se define el peso que acompanara la funcion evaluada de 1 a N
#para los extremos es h/2 y para los otros elementos h
def weights(h,i,N):
	
	if i==1 or i==N:
			w=h/2
	else:
			w=h
	return w
	
def trapezoid_rule(a,b,N,f):
	h=(b-a)/(N-1)
	suma=0.0
	for i in range(1,N+1):
		w = weights(h,i,N)
		t=a+(i-1)*h
		suma+=(w*f(t))
	print suma

	
trapezoid_rule(lower_limit, upper_limit, N, funcion)



