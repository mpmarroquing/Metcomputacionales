import math
import numpy as np

#calcular la integral
def legendre(x):
	return (abs((5*x**3 - 3*x)/2))**2
	
min_x = -1
max_x = 1

x = np.random.random(1000000) * ( max_x - min_x) + min_x
y = legendre(x)

integral = np.average(y)* ( max_x - min_x)

print "integral=",integral

#usar error porcentual
v_analitico = (2.0/7.0)


print "e%=",(((v_analitico-integral)/v_analitico)*100)
