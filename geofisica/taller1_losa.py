import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(-100,100,500)
G=6.67*10**(-11)
z1=10
z2=12
z3=15
d1=2900
d2=2300
d3=2800
h1=2
h2=3
h3=4
ds=2670
PI=3.14159

def anomalia1(x):
	return (2*G*h1*(d1-ds)*((PI/2)+np.arctan(x/z1)))*100000
	
def anomalia2(x):
	return (2*G*h2*(d2-ds)*(PI/2+np.arctan(x/z2)))*100000

def anomalia3(x):
	return (2*G*h3*(d3-ds)*(PI/2+np.arctan(x/z3)))*100000
	
function1=anomalia1(x)
plt.plot(x,function1, label="z=10,d=2900,h=2")
plt.title("Anomalia Gravimetrica Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.savefig("anom1.png")
plt.show()

function2=anomalia2(x)
plt.plot(x,function2, label="z=12,d=2300,h=3")
plt.title("Anomalia Gravimetrica Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.savefig("anom2.png")
plt.show()

function3=anomalia3(x)
plt.plot(x,function3, label="z=15,d=2800,h=4")
plt.title("Anomalia Gravimetrica Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.savefig("anom3.png")
plt.show()
n_points = 500
h = np.logspace(-12, -1, n_points)

def forward(fun, x, h):
    return (fun(x+h) - fun(x))/h
    
def forward2(fun,x,h):
	return (fun(fun(x+h)+fun(h))-fun(fun(x)))/h
    
dev1_a1= forward(anomalia1, x, h)

dev2_a1= forward2(anomalia1, x, h)

dev1_a2= forward(anomalia2, x, h)

dev1_a3= forward(anomalia3, x, h)

plt.plot(x,dev1_a1,label="ANOMALIA1") 
plt.title("Primera derivada Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.savefig("deriv_anom1.png")
plt.show()

plt.plot(x,dev1_a2,label="ANOMALIA2") 
plt.title("Primera derivada Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.savefig("deriv_anom2.png")
plt.show()

plt.plot(x,dev1_a3,label="ANOMALIA3") 
plt.title("Primera derivada Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.savefig("deriv_anom3.png")
plt.show()

plt.plot(x,dev2_a1, label="ANOMALIA1")
plt.title("Segunda derivada Losa horiz semi-infinita")
plt.ylabel("DELTAg(mGal)")
plt.xlabel("distancia x (m)")
plt.legend(loc="lower right")
plt.show()