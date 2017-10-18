#esta funcion recibe un numero entero positivo e imprime 1 si el numero es primo y 0 de lo contrario



def is_prime(n):
	k=0
	for i in range(2,n):
 		if (n%i==0) and i!=n and k!=1:
			k=0
			break
		else:
			k=1	
	print k
			
is_prime(19)