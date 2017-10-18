import numpy as np

data=np.genfromtxt("room-temperature.csv", usecols=(1,2,3,4),skip_header=1,delimiter=",")
data2=data.transpose()

def matriz_cov(m1,m2):
	for i in range (4):
		suma1=0.0
		media1= len(m1[:,i])/

