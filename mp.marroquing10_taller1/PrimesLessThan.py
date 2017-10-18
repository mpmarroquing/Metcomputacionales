#esta funcion recibe un numero entero positivo e imprime todos los primos menores a el.

primos=[]
no_primos=[]

def PrimesLessThan(m):
	for i in range(2,m):
		for n in range (2,m):
			if (i%n==0) and i!=n:
				no_primos.append(i)
		if i not in no_primos and i not in primos:
			primos.append(i)
	print primos
	
PrimesLessThan(7)