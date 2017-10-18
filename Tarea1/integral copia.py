import numpy as np

a=0
b=1
c=0
d=3.1415
n=1000
m=1000

x=[]
y=[]

def funcion(x,y):
	return (x+np.cos(y)*x)**3

f_eval1 =[]
def montecarlo(f, a, b, c, d,n,m):    
    y = np.random.random(n)*(b-a)+a
    x = np.random.random(m)*(d-c)+c
    f_eval1.append(f(x,y))
    f_eval=np.array(f_eval1)
    result =(b-a)*(d-c)*np.mean(f_eval)
    return result
    
print "El valor de la integral por el metodo de montecarlo es", montecarlo(funcion, a, b,c,d,n,m)


# Calcular la integral usando metodo de trapezoides

def trapezoid(f, a, b, c, d, N, M):
    x = np.linspace(a, b, N+1)
    y = np.linspace(c, d, M+1)
    h = (b-a)/N
    k = (d-c)/M
    result = 0.0
    for i in range(0,N):
    	for j in range(0,M):
        	if i == 0 or i == n or j==M:
            		weight = (h*k)/4
        	else:
        		if i == N/2 and j == M/2 :
    		    		weight = (h*k)
            		else:
            			weight = (h*k)/2
    	result += f(x[i],y[j])*weight
	return result
    
print trapezoid(funcion, a, b, c, d, 100,100)