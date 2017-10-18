#esta funcion recibe un arreglo de enteros + e imprime un arreglo pix.

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.special
import math
from math import log


x= np.arange(1000)
y=[]
k=[]
primos=[]
no_primos=[]
z=0

def NumberPrimesLessThan(x):
	for j in range (0,len(x)):
		m=x[j]
		for i in range(2,m):
			for n in range (2,m):
				if (i%n==0) and i!=n:
					no_primos.append(i)
			if i not in no_primos and i not in primos:
				primos.append(i)
		z=len(primos)
		y.append(z)
	print [x,y]
	
NumberPrimesLessThan(x)


plt.plot (x,y, label="Primes Less Than (x)")
plt.plot (x,scipy.special.expi(np.log(x)), label="log(x)")
plt.title("Ajuste corresponde")
plt.show()