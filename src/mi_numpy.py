import numpy as np

a = np.array([1, 2, 3, 4, 5])
#sumar 2 a cada elemento del array
a = a * 2
#calcular la suma del arreglo
sum_a = np.sum(a)
#calcular el promedio del arreglo
promedio_a = np.mean(a)
print(np.__version__)
print(a)
print(sum_a)
print(promedio_a)

#enunciado:
#crea una matriz de 3 filas y 3 columnas llena de 1 y que primero muestre la llena de 1 y despues las demas:
#cambia todos los valores a 5
#calcula el valor máximo de la matriz
#calcula la suma de cada columna
#la solucion es :
matriz = np.ones((3, 3))
print(matriz)
matriz = matriz * 5
print(matriz)
maximo = np.max(matriz)
print(maximo)
suma_columnas = np.sum(matriz, axis=0)
print(suma_columnas)