Dimension = 0
while Dimension <= 1 or Dimension % 2 == 0:
    Dimension = int(input("Ingrese un número positivo impar para determinar la dimension del cuadrado mágico: "))

PuntoInicial = int(Dimension / 2)
CuadradoMagico = [[0 for d in range(Dimension)] for d in range(Dimension)]
CuadradoMagico[0][PuntoInicial] = 1

cont = 1
x = 0
y = PuntoInicial

while cont != (Dimension * Dimension):
    cont += 1
    newx = x
    x -= 1
    newy = y
    y -= 1

    if x < 0:
        x = Dimension - 1
    if y < 0:
        y = Dimension - 1

    if CuadradoMagico[x][y] == 0:
        CuadradoMagico[x][y] = cont
    else:
        x += 1
        if x > 0:
            x = newx + 1
        y = newy
        CuadradoMagico[x][y] = cont

matrix = len(CuadradoMagico)
for i in range(matrix):
    print(CuadradoMagico[i])
