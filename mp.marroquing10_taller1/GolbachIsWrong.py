#esta funcion imprime el primer numero que viola la conjetura de Goldbach.
import numpy as np
import math

def is_prime(n):
	k=0
	for i in range(2,n):
 		if (n%i==0) and i!=n and k!=1:
			k=0
			break
		else:
			k=1	
	return k
			
primos=[]
no_primos=[]

def PrimesLessThan(m):
	for i in range(2,m):
		for n in range (2,m):
			if (i%n==0) and i!=n:
				no_primos.append(i)
		if i not in no_primos and i not in primos:
			primos.append(i)
	return primos
	

	

for i in range(0,6000):
	k=0.0
	z="o"
	if is_prime(i)!=1 and i%2!=0:
		a=PrimesLessThan(i)
		for j in range(0, len(a)):
			if (math.sqrt((i-a[j])/2)).is_integer()==True:
				i=i+1
			else: 
				z="i"
				break
				print z


#def GoldbachIsWrong(x):
	#n=[0,1000]
	#for j in range (0,x):
	#	if is_prime(j)!=1 and j%2!=0:
	#		a=PrimesLessThan(1000)
		#	for i in range(0,len(n)):
		#		for m in range(0,len(a)):
		#			if x==a[m]+2*(n[i]**2):
		#				print "TRUE"
		#				break
		#		else:
		#			print "false"
	#				break
									
#GoldbachIsWrong(100)