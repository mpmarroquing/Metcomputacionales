import numpy as np
from scipy import linalg as la
import matplotlib.pyplot as plt

#guardar y normalizar los datos
data=np.genfromtxt("siliconwaferthickness.csv",delimiter=",",skip_header=1)
data2=np.zeros(np.shape(data))

for i in range(9):

	data2[:,i]= ( data[:,i] - np.mean(data[:,i]) ) /( np.std(data[:,i]) )


pto1 = data2[:,0]
pto2 = data2[:,1]
pto3 = data2[:,2]
pto4 = data2[:,3]
pto5 = data2[:,4]
pto6 = data2[:,5]
pto7 = data2[:,6]
pto8 = data2[:,7]
pto9 = data2[:,8]

#grafica de los datos
x=np.arange(0,184)
plt.plot(x,pto1,c="red",label="G1")
plt.plot(x,pto2,c="yellow",label="G2")
plt.plot(x,pto3,c="blue",label="G3")
plt.plot(x,pto4,c="black",label="G4")
plt.plot(x,pto5,c="purple",label="G5")
plt.plot(x,pto6,c="green",label="G6")
plt.plot(x,pto7,c="gray",label="G7")
plt.plot(x,pto8,c="orange",label="G8")
plt.plot(x,pto9,c="brown",label="G9")
plt.title("Exploracion Datos")
plt.legend()
plt.savefig("ExploracionDatos.pdf")

plt.close()




#calcular la matriz de covarianza


def matrizcov(m):
	tam=np.shape(data2)[1]
	matrizc=np.zeros((tam,tam))
	for i in range (0,tam):
		for j in range(0,tam):
				cova=(m[:,i]*m[:,j])
				matrizc[i,j]=np.mean(cova)
	return matrizc

 
matriz_cov = matrizcov(data2)


#autovalores y autovectores
valores_pr,vectores_pr=np.linalg.eig(matriz_cov)

val_prop_in = (np.argsort(-valores_pr))



valores_pr_or = valores_pr[val_prop_in]
vectores_pr_or = vectores_pr[val_prop_in]

print "Considero que se necesitan 3 componentes para describir la variabilidad de los datos"

#graficar los dos componentes

datos_n = np.dot(vectores_pr_or.T,data2.T)
plt.scatter(datos_n[0,:],datos_n[1,:])
plt.xlabel("componente principal 1")
plt.ylabel("componente principal 2")
plt.title("PCA datos")
plt.savefig("PCAdatos.pdf")
plt.show()

#graficar agrupaciones
			
plt.scatter(vectores_pr_or[0,0],vectores_pr_or[0,1],label="G1",c="red",s=100)
plt.scatter(vectores_pr_or[1,0],vectores_pr_or[1,1],label="G2",c="blue",s=100)
plt.scatter(vectores_pr_or[2,0],vectores_pr_or[2,1],label="G3",c="yellow",s=100)
plt.scatter(vectores_pr_or[3,0],vectores_pr_or[3,1],label="G4",c="purple",s=100)
plt.scatter(vectores_pr_or[4,0],vectores_pr_or[4,1],label="G5",c="black",s=100)
plt.scatter(vectores_pr_or[5,0],vectores_pr_or[5,1],label="G6",c="green",s=100)
plt.scatter(vectores_pr_or[6,0],vectores_pr_or[6,1],label="G7",c="orange",s=100)
plt.scatter(vectores_pr_or[7,0],vectores_pr_or[7,1],label="G8",c="brown",s=100)
plt.scatter(vectores_pr_or[8,0],vectores_pr_or[8,1],label="G9",c="gray",s=100)
plt.legend()
plt.xlabel("componente principal 1")
plt.ylabel("componente principal 2")
plt.title("Agrupacion de datos")
plt.savefig("PCAvariables.pdf")
plt.close()

print "Las variables que estan correlacionadas son G1,G2,G3,G4 y G9, que corresponden al grosor1,2,3,4 y 9 de la waffer"