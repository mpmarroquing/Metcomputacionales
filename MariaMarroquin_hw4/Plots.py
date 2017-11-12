import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile

amp_ef = np.genfromtxt("datos_cuerda_ef.dat")

x_ef = np.genfromtxt("cond_ini_cuerda.dat")[:,0]
y_ef = np.genfromtxt("cond_ini_cuerda.dat")[:,1]

tambor = np.genfromtxt("cond_ini_tambor.dat")

amp_es = np.genfromtxt("datos_cuerda_es.dat")

#grafica cuerda extremos fijos
plt.plot(x_ef,amp_ef[(50000*129):(50000*129+129)],label="1/2")     		#1/2
plt.plot(x_ef,amp_ef[(12500*129):(12500*129+129)],label="1/8")			#1/8
plt.plot(x_ef,amp_ef[(25000*129):(25000*129+129)],label="1/4")			#1/4
plt.plot(x_ef,amp_ef[:129],label="0")									#0
plt.legend()
plt.title("Cuerda con extremos fijos")
plt.xlabel("posicion")
plt.ylabel("amplitud")
plt.savefig("cuerda_ef.pdf")
plt.close()

#sonido

datos = np.zeros(100000)
for i in range(100000):
	datos[i] = amp_ef[int(129*i/2)]
	
scipy.io.wavfile.write("sonido.wav",99999,datos)

#grafica cuerda perturbada
plt.plot(x_ef,amp_es[(50000*129):(50000*129+129)],label="1/2")     		#1/2
plt.plot(x_ef,amp_es[(12500*129):(12500*129+129)],label="1/8")			#1/8
plt.plot(x_ef,amp_es[(25000*129):(25000*129+129)],label="1/4")			#1/4
plt.plot(x_ef,amp_es[:129],label="0")									#0
plt.title("Cuerda con un extremo perturbado")
plt.xlabel("posicion")
plt.ylabel("amplitud")
plt.legend()
plt.savefig("cuerda_es.pdf")
plt.close()

#tambor
amp_tam = np.genfromtxt("datos_tambor.dat")

plt.plot(amp_tam[(50000*129):(50000*129+129)][(50000*129):(50000*129+129)],label="1/2")     		#1/2
plt.plot(amp_tam[(12500*129):(12500*129+129)][(12500*129):(12500*129+129)],label="1/8")			#1/8
plt.plot(amp_tam[(25000*129):(25000*129+129)][(25000*129):(25000*129+129)],label="1/4")			#1/4
plt.plot(amp_tam[:129][:129],label="0")									#0
plt.title("Tambor")
plt.xlabel("posicion")
plt.ylabel("amplitud")
plt.legend()
plt.savefig("tambor.pdf")
plt.close()
