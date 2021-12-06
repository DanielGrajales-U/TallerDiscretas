#


# Ejercicio: crear un conjunto y comprobar si
# sacando dos conjuntos con elementos del conjunto madre y sumandolos da el mismo resultado


# Variable para pedir el tamaño del conjunto
n = int(input("Ingrese el tamaño que desea su conjunto: "))
# Lista donde se alamacena el conjunto Total
listaNum = []

# Bucle para añadir elementos a la lista
for i in range(n + 1):
    listaNum.append(i)

print(listaNum)

# funcion para comprobar si se cumple lo pedido


def sumar(lista):
    if lista == []:
        suma = 0
    else:
        suma = lista[0] + sumar(lista[1:])

    return suma


print(sumar(listaNum))
