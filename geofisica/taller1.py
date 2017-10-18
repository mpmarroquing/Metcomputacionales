import matplotlib.pyplot as plt
import numpy as np
import math

#PARA ESFERA
x=np.linspace(-30,30,500)
G=6.67*10**(-11)
r=3
z1=3
z2=5
z3=4
de=1900
ds=2670
PI=3.14159

def anomalia1(x):
	return ((4/3)*PI*G*(r**3)*(2900-ds)*(z1/((x**2)+(z1**2))**(3/2)))*100000
def anomalia2(x):

	return (4/3)*PI*G*(r**3)*(2900-ds)*(z2/((x**2)+(z2**2))**(3/2))*100000
def anomalia3(x):
	return (4/3)*PI*G*(r**3)*(de-ds)*(z3/((x**2)+(z3**2))**(3/2))*100000

function1=anomalia1(x) 
function2=anomalia2(x) 
function3=anomalia3(x) 

#half-width anomalia 1

i0=np.where(anomalia1(x)==np.max(anomalia1(x)))
ic=(i0[0])
ica=ic[1]
gmed1 = (np.max(anomalia1(x)))/2
i=np.where((anomalia1(x)>=(gmed1-0.001)) & (anomalia1(x)<=(gmed1+0.001)))
im=(i[0])
ima=(im[2])


i02=np.where(anomalia2(x)==np.max(anomalia2(x)))
ic2=(i02[0])
ica2=ic2[1]
gmed2 = (np.max(anomalia2(x)))/2
i2=np.where((anomalia2(x)>=(gmed2-0.0001)) & (anomalia2(x)<=(gmed2+0.0001)))
im2=(i2[0])
ima2=(im2[1])

i03=np.where(-anomalia3(x)==np.max(-anomalia3(x)))
ic3=(i03[0])
ica3=ic3[1]
gmed3 = (np.max(-anomalia3(x)))/2
i3=np.where((-anomalia3(x)>=(gmed3-0.001)) & (-anomalia3(x)<=(gmed3+0.001)))
im3=(i3[0])
ima3=(im3[1])



plt.plot(x,function1,label="z=3m")
plt.plot(x,function2,label="z=5m") 
plt.plot(x,function3, label="z=4m , de < ds")
plt.title("Anomalia Gravimetrica Esfera")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.scatter(x[ica], gmed1,label="HW=2.885771")
plt.scatter(x[ica2], gmed2,c="green",label="HW=4.929859")
plt.scatter(-x[ica3], -gmed3, c="red",label="HW=3.967935")
plt.legend(loc="lower left")

plt.savefig("esferas.pdf") 
plt.show()



#PARA CILINDROS

x=np.linspace(-10,10,100)
G=6.67*10**(-11)
r=3
z1=3
z2=5
z3=4
dc=1900
ds=2670
PI=3.14159

def anomalia1c(x):
	return 2*PI*G*(r**2)*(2900-ds)*(z1/((x**2)+(z1**2)))*100000
def anomalia2c(x):
	return 2*PI*G*(r**2)*(2900-ds)*(z2/((x**2)+(z2**2)))*100000
def anomalia3c(x):
	return 2*PI*G*(r**2)*(dc-ds)*(z3/((x**2)+(z3**2)))*100000

function1c=anomalia1c(x) 
function2c=anomalia2c(x) 
function3c=anomalia3c(x) 

i0=np.where(anomalia1c(x)==np.max(anomalia1c(x)))
ic=(i0[0])
ica=ic[1]
gmed1 = (np.max(anomalia1c(x)))/2
i=np.where((anomalia1c(x)>=(gmed1-0.001)) & (anomalia1c(x)<=(gmed1+0.001)))
im=(i[0])
ima=(im[2])
print x[ima]+x[ica]

i02=np.where(anomalia2c(x)==np.max(anomalia2c(x)))
ic2=(i02[0])
ica2=ic2[1]
gmed2 = (np.max(anomalia2c(x)))/2
i2=np.where((anomalia2c(x)>=(gmed2-0.0001)) & (anomalia2c(x)<=(gmed2+0.0001)))
im2=(i2[0])
ima2=(im2[1])
print x[ima2]+x[ica2]

i03=np.where(-anomalia3c(x)==np.max(-anomalia3c(x)))
ic3=(i03[0])
ica3=ic3[1]
gmed3 = (np.max(-anomalia3c(x)))/2
i3=np.where((-anomalia3c(x)>=(gmed3-0.001)) & (-anomalia3c(x)<=(gmed3+0.001)))
im3=(i3[0])
ima3=(im3[1])
print x[ima3]+x[ica3]

plt.plot(x,function1c, label="z=3m")
plt.plot(x,function2c, label="z=5m") 
plt.plot(x,function3c, label="z=4m, de < ds")
plt.title("Anomalia Gravimetrica Cilindro")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.scatter(x[ica], gmed1,label="HW=3.030")
plt.scatter(x[ica], gmed2,label="HW=5.050",c="green")
plt.scatter(-x[ica], -gmed3,label="HW=4.040",c="red")
plt.legend(loc="lower left")
plt.savefig("cilindros.pdf") 

plt.show() 

