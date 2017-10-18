#este script toma una matriz cuadrada y aplica el sistema de eliminacion gaussiana
import numpy as np
import matplotlib.pyplot as plt


ma =np.array(([4,2,1],[25,5,1],[81,9,1]))
v=[45.948,119.985,231.497]
print "ma*a=v","donde a es el vector de aceleraciones"

def eliminacion_g (m,vec):
	m=np.float_(m)
	vec=np.float_(vec)
	for i in range(0,len(vec)):	
		vec[i] = vec[i]/m[i,i]
		m[i,:] = m[i,:]/m[i,i]					#unos en la diagonal
		
		
		for j in range(i+1,len(vec)):
			vec[j] = vec[j] - m[j,i]* vec[i]
			m[j,:] = m[j,:] - m[j,i]* m[i,:]			#ceros
	

	
	return m,vec
	

mat,vect = eliminacion_g(ma,v)

a3=vect[2]
a2=vect[1]-mat[1,2]*a3
a1=vect[0]-mat[0,1]*a2-mat[0,2]*a3


t=[2,5,9]
p1=a1*t[0]**2+a2*t[0]+a3
p2=a1*t[1]**2+a2*t[1]+a3
p3=a1*t[2]**2+a2*t[2]+a3
p=[p1,p2,p3]
plt.plot(t,p,label="v = 0.457t^2 + 21.48t +1.16",c="green")
plt.scatter(t,p)
plt.xlabel("Tiempo(s)")
plt.ylabel("Velocidad(m/s)")
plt.legend(loc="upper left")
plt.title("Velocidad del Cohete")
plt.savefig("VelocidadCohete.pdf")
plt.close()

#velocidad en tiempo 7
T=7
V7= a1*T**2 + a2*T + a3
print "a es igual a:", a1,a2,a3
print "La Velocidad a los 7 segundos es", V7

