n = int(input('Ingrese un numero par:'))
while n<0 or n%2==1:
    n = int(input('Ingrese un numero par:'))

matriz = []
row = []
counter = 0
for j in range(0,n):
    fila = []
    if j == 0:
        for i in range(1, n+1):
            row.append(i)
        matriz.append(row)
    elif j<(n/2):
        for i in range(0,n):
            fila.append(row[int(i)]+2*n*j)
        matriz.append(fila) 
    else:
        for i in range(0,n):
            fila.append(row[int(i)]+n*(n-counter))
        matriz.append(fila)
        counter+=2
for m in matriz:
    print(m)
