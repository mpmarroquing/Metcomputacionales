import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt
import csv

#estandarizar los datos
data=np.loadtxt("DataCredit.csv")
data2=np.zeros(np.shape(data))

for i in range(7):

	data2[:,i]= ( data[:,i] - np.mean(data[:,i]) )/( np.std(data[:,i]) )

print data2


#hacer la matriz de covarianza
matriz_cov = np.cov(data2.T)


#componentes principales y grafica
valores_pr,vectores_pr=np.linalg.eig(matriz_cov)

val_prop = abs(np.sort(-valores_pr))





x=[1,2,3,4,5,6,7]
plt.scatter(x,val_prop)
plt.show()


#porcentaje de variavilidad
suma=0.0
for i in range (0,7):
	suma= suma + val_prop[i]

	
suma2=0.0	
for i in range(0,4):
	suma2+= val_prop[i]


print "El porcentaje de variabilidada es:", suma/suma2

#variables correlacionadas
print abs(vectores_pr)
print "Income, Limit, Balance"