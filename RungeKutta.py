import numpy as np
import matplotlib.pyplot as plt

min_x=0.001
max_x=20
h=0.01
n_points=int((max_x-min_x)/h)
x=np.zeros(n_points)
y1=np.zeros(n_points)
y2=np.zeros(n_points)

def func_prima_1(x,y1,y2):							
	return y2							

def func_prima_2(x,y1,y2):
	return (-1)*(x*y2+(x**2)*y1+0.99*y2**2)/x**2

def RungeKutta4or(x_old,y1_old,y2_old):

	
	k1_p1=func_prima_1(x_old,y1_old,y2_old)
	k1_p2=func_prima_2(x_old,y1_old,y2_old)
	
	
	x1 = x_old + (h/2.0)
	y1_1 = y1_old + (h/2.0) * k1_p1
	y2_1 = y2_old + (h/2.0) * k1_p2
	k2_p1 = func_prima_1(x1,y1_1,y2_1)
	k2_p2 = func_prima_2(x1,y1_1,y2_1)
	
	
	x2 = x_old + (h/2.0)
	y1_2 = y1_old + (h/2.0)*k2_p1
	y2_2 = y2_old + (h/2.0)*k2_p2
	k3_p1 = func_prima_1(x2,y1_2,y2_2)
	k3_p2 = func_prima_2(x2,y1_2,y2_2)
	
	
	x3 = x_old + h
	y1_3 = y1_old + h*k3_p1
	y2_3 = y2_old + h*k3_p2
	k4_p1 = func_prima_1(x3,y1_3,y2_3)
	k4_p2 = func_prima_2(x3,y1_3,y2_3)
	
	
	prom_k_p1 = (1.0/6.0)*(k1_p1 + 2.0*k2_p1 + 2.0*k3_p1 + k4_p1)
	prom_k_p2 = (1.0/6.0)*(k1_p2 + 2.0*k2_p2 + 2.0*k3_p2 + k4_p2)
	
	x_nw = x_old + h
	y1_nw = y1_old + h*prom_k_p1
	y2_nw = y2_old + h*prom_k_p2
	
	return x_nw,y1_nw,y2_nw
	
x[0]=min_x
y1[0]=1.0
y2[0]=0.0


for i in range(1,n_points):
	x[i],y1[i],y2[i] = RungeKutta4or(x[i-1],y1[i-1],y2[i-1])

plt.plot(x,y1)
plt.show()