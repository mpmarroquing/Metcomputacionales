#este script toma una matriz cuadrada y aplica el sistema de eliminacion gaussiana
import numpy as np

ma =np.array(([2,1,2],[6,3,1],[6,2,4]))

def eliminacion_g (m):
	
	for i in range(0,len(m)):	
	
		m[i,:] = m[i,:]/m[i,i]						#unos en la diagonal

		for j in range(i+1,len(m)):
			m[j,:] = m[j,:] - m[j,i]* m[i,:]			#
			
					
	
	return m
	
print eliminacion_g(ma)
print np.linalg.solve(ma)