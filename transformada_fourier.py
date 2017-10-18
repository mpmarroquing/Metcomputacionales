#este script implementa la transformada de fourier para funciones discretas
import numpy as np
import math
import matplotlib.pyplot as plt

pi=3.1415
a=-2*pi
b=2*pi
x=np.linspace(a,b,30)

def function1(x):
	return np.cos(x)

H = []
H = function1(x)	
N = 30

def trans_fourier(list,N):
	a=[]
	sum=0.0
	for k in range (0, len(list)):
		for n in range (0,N):
			sum+= list[n]*np.exp(-2*pi*1j*k*n/N)
		a.append(sum)
	return a
	
plt.plot(x,trans_fourier(H,N))
plt.show()


