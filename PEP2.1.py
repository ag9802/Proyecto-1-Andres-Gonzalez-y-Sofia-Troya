def suma_digitos_al_cuadrado( number ):
    suma_digitos = 0
    for num in range(len(str(number))):

        suma_digitos += int(str(number)[num])**2
    return suma_digitos

N = int(input('Ingrese un numero entero positivo:'))
N_minior_counter = 0
iteration_counter = 0 
for i in range (N):
    Aux_N = i + 1


    while (Aux_N != 1 and Aux_N != 89):
        iteration_counter += 1
        Aux_N = int(suma_digitos_al_cuadrado(Aux_N))
        if Aux_N == 89:
            N_minior_counter += 1
            Aux_N2 = i +1

print('Desde 1 hasta ', N, 'hay', N_minior_counter, 'numeros que llega a 89')
print('Obteniendose que el porcentaje de numeros que llegan a 89 es el', round(N_minior_counter*100/N,2), '%')