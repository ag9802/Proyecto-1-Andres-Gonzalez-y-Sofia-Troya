# Problema II
Hole_Size = int(input('Ingrese el tamaño de profundidad del pozo:'))
amount_that_climbing= int(input('Ingrese la cantidad que trepaba durante el dia:'))
quantify_that_descend= int(input('Ingrese la cantidad que desciende durante la noche:'))

condiction_1 = amount_that_climbing - quantify_that_descend

while condiction_1 != Hole_Size-1:
    if condiction_1 <= Hole_Size-1:
        print('El caracol tardo aproximadamente:',condiction_1, 'Dias en salir del Pozo')
        condiction_1 = condiction_1 + 1
    else:
        print('Error, el caracol no pudo salir del pozo')
        break
        



