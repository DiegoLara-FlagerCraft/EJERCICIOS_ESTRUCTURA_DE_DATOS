import random
ListaFilCol = []
ListaColFil = []
Dimension = 3
Matriz = [[0 for x in range(Dimension)] for y in range(Dimension)]
for x in range(0, Dimension):
    for y in range(0, Dimension):
        Matriz[x][y] = int(random.randint(1, 99))

Arreglo = len(Matriz)
for i in range(Arreglo):
    print(Matriz[i])

print("\nDE MATRIZ A LISTA \n")

for x in range(0, Dimension):
    for y in range(0, Dimension):
        ListaFilCol.append(Matriz[x][y])
print(ListaFilCol)

for x in range(0, Dimension):
    for y in range(0, Dimension):
        ListaColFil.append(Matriz[y][x])
print(ListaColFil)