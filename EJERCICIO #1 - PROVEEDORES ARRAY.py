Opcion = 0
Pos = 0
Proveedores = ["FLAGER", "CRAFT", "POSTOBON", "NORMA"]
Ciudades = ["BUCARAMANGA", "PIEDECUESTA", "FLORIDABLANCA", "GIRON"]
NumeroArticulos = [20, 50, 10, 30]
Ids = [2020, 1587, 623, 58]
Nombres = ["ALCOHOL", "DULCES", "GASEOSA", "PAPEL"]
Valores = [200000, 60000, 50000, 4000]

while Opcion != 7:
    Pos = 0
    Opcion = int(input("Ingrese el numero de la opcion que desea realizar \n"
                       "1 - Lista de Proveedores \n"
                       "2 - Ingresar Nuevo Proveedor \n"
                       "3 - Información del Proveedor \n"
                       "4 - Actualizar Ciudad del Proveedor \n"
                       "5 - Actualizar articulos del Proveedor \n"
                       "6 - Eliminar Proveedor \n"
                       "7 - Salir del Programa \n"))
    print("\n")

    if Opcion == 1:
        print(Proveedores)
        print("\n")


    if Opcion == 2:
        print("INFORMACIÓN DEL PROVEEDOR")
        Proveedor = str(input("Ingrese el nombre del nuevo Proveedor: "))
        Proveedores.append(Proveedor)
        Ciudad = str(input("Ingrese la ciudad en la que esta ubicada el proveedor: "))
        Ciudades.append(Ciudad)
        NumeroArtic = int(input("Ingrese el numero de articulos que provee el proveedor: "))
        NumeroArticulos.append(NumeroArtic)
        print("INFORMACIÓN DEL ARTICULO")
        Id = int(input("Ingrese el ID del articulo: "))
        Ids.append(Id)
        Nombre = str(input("Ingrese el nombre del articulo: "))
        Nombres.append(Nombre)
        Valor = int(input("Ingrese el valor del Articulo: "))
        Valores.append(Valor)
        print("\n")

    if Opcion == 3:
        Pos = Proveedores.index(str(input("Ingrese el nombre del Proveedor: ")))
        print("INFORMACION DEL PROVEEDOR")
        print("NOMBRE = ", Proveedores[Pos])
        print("CIUDAD = ", Ciudades[Pos])
        print("NUMERO DE ARTICULOS = ", NumeroArticulos[Pos])
        print("INFORMACION DEL ARTICULO")
        print("ID = ", Ids[Pos])
        print("NOMBRE = ", Nombres[Pos])
        print("VALOR = ", Valores[Pos])
        print("\n")

    if Opcion == 4:
        Pos = Proveedores.index(str(input("Ingrese el nombre del Proveedor que cambio de ciudad: ")))
        Ciudades[Pos] = str(input("Ingrese la ciudad a la cual se mudo el proveedor: "))
        print("\n")

    if Opcion == 5:
        Pos = Proveedores.index(str(input("Ingrese el nombre del Proveedor que cambio el numero de articulos: ")))
        NumeroArticulos[Pos] = str(input("Ingrese el nuevo numero de articulos del proveedor: "))
        print("\n")

    if Opcion == 6:
        Pos = Proveedores.index(str(input("Ingrese el nombre del Proveedor que desea eliminar: ")))
        Proveedores.pop(Pos)
        Ciudades.pop(Pos)
        NumeroArticulos.pop(Pos)
        Ids.pop(Pos)
        Nombres.pop(Pos)
        Valores.pop(Pos)



print(Proveedores)
print(Ciudades)
print(NumeroArticulos)
print(Ids)
print(Nombres)
print(Valores)
