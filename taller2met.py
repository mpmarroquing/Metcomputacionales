import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
from scipy import special, optimize

PI = 3.14159
lower_limit_x = 0.0
upper_limit_x = 10.0
lower_limit_y = 0.0
upper_limit_y = 10.0


# funcion a integrar
def function(x,y):
    return (4/PI)*np.exp((-x**2)-(y**2))

# Solucion analitica
def exact():
    return (scipy.special.erf(10)-scipy.special.erf(0))**2

# Calculamos el error absoluto entre el valor real de la integral y el calculado por los diferentes metodos.
def error(real, calculated):
    return abs((real-calculated)/real)

    
# Calcular la integral usando MonteCarlo
def montecarlo(f, a, b, c, d, n, m):    
    x = np.random.random(n)
    y = np.random.random(m)
    f_eval = f(x,y)
    result = (b-a)*(c-d)*f_eval.mean()
    return np.log10(n)+np.log10(m), result

# Calcular la integral usando metodo de trapezoides
def trapezoid(f, a, b, c, d, n, m):
    x = np.linspace(a, b, n+1)
    y = np.linspace(a, b, m+1)
    h = (b-a)/n
    k = (d-c)/m
    result = 0
    for i in range(n+1):
    	for j in range(m+1):
        	if i == 0 or i == n or j==m:
            		weight = (h*k)/4
        	else:
        		if i == n/2 and j == m/2 :
    		    		weight = (h*k)
            		else:
            			weight = (h*k)/2
    		result += f(x[i],y[j])*weight
    return np.log10(n)+np.log10(m), result
    
# Vamos a calcular la integral
def integrate(func, a, b, c, d, n, m):
    # Llamamos todas la funciones que creamos para calcular la integral. Recordemos que estas funciones retornan dos numeros: el primero es el logaritmo del numero entero usado para integrar y segundo es el valor de la integral calculado.
    montecarlo_results = montecarlo(func, a, b, c, d, n, m)
    trapezoid_results = trapezoid(func, a, b, c, d, n, m)

# creamos una lista con los resultados de las 4 funciones
    results = [montecarlo_results, trapezoid_results]
    #en la lista "numbers" guardamos los resultados de las integrales por los diferentes metodos
    numbers = [item[0] for item in results]
    #en la lista "errors" guaramos el error de nuestro calculo con respecto al valor exacto de la integral.
    errors = [np.log10(error(exact_value, item[1])) for item in results]
    
    
    return numbers, errors

#este sera el calor exacto de la integral
exact_value = exact ()

   
#creamos una lista de 20 puntos entre 0 y 10^6
points = 20
numbers = np.linspace(1, 3, points)


#estas listas vacias las usaremos para guardar nuestros valores finales
values_buffer = [[],[]]
numbers_buffer = [[],[]]

#estos nombres los usaremos para etiquetar las graficas
names = ["MonteCarlo","Trapezoid"]

#Ahora implementaremos la funcion "integrate" 20 veces recorriendo 6 ordenes de magnitud.
for n in numbers:
    numbers, results = integrate(function, lower_limit_x, upper_limit_x, lower_limit_y, upper_limit_y, int(n), int(n))
    for (values_list, numbers_list, number, result) in zip(values_buffer, numbers_buffer, numbers, results): #Explicar como funciona "for" "in zip".
        values_list.append(result)
        numbers_list.append(number)
        
# Graficamos
for (values_list, numbers_list, name) in zip(values_buffer, numbers_buffer, names):
    plt.plot(numbers_list, values_list, "-o", label=name)

plt.legend(loc=3)
plt.xlabel("$\log_{10}n$")
plt.ylabel("$\log_{10}\epsilon$")
plt.grid()
plt.show()
    
    