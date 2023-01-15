n = int(input('Ingrese el numero de filas:'))
m = int(input('Ingrese el numero de columna:'))

matriz = []
for j in range (0,n):
    fila = []
    for i in range(0,m):
        fila.append(1 +(m*j)+ i)
    if j%2 == 1:
        fila.reverse()

    matriz.append(fila)
for x in matriz:
    print(x)