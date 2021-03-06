class Node:
    def __init__(self, object):
        self.object = object
        self.Next = None

class ListaEnlazada:
    def __init__(self):
        self.Head = None
        self.Tail = None

        # Revisar si la Lista esta vacia
    def isEmpty(self):
        return self.Head

        # Agrega un elemento al final de la lista.
        # @ param object elemento
        # @ return
    def add(self, object):
        try:
            node = Node(object)
            if not self.isEmpty():
                self.Head = node
                self.Tail = node
            else:
                Route = self.Head
                while Route != None:
                    Route = Route.Next
                self.Tail.Next = node
                self.Tail = node
        except:
            return False


        # Inserta un elemento en una posición siguinete al nodo especificado.
        # @ param node nodo
        # @ param object elemento
        # return
    def add2(self, element, pos):
        try:
            node = Node(object)
            if not self.isEmpty():
                self.Head = node
                self.Tail = node
            else:
                cont = self.Head
                Tam = 1
                while cont:
                    Prev = cont
                    ant = cont.Next
                    cont = cont.Next
                    Tam += 1
                    if Tam == pos:
                        cont.object = element
                        self.Tail = cont.object
                        ant.object = self.Tail.Next
                        break

        except:
            return False


        # Agrega todos los elementos al final de la lista.
        # @ param objects elementos
        # @ return
    def addAll(self, element1, element2, element3):
        List.add(element1)
        List.add(element2)
        List.add(element3)


        # Inserta todos los elementos desde una posición siguinete al nodo especificado.
        # @ param node nodo
        # @ param objects elementos
        # @ return
    def addAll2(self, element1, element2, element3, pos):
        List.add2(element2, pos)
        List.add2(element1, pos)
        List.add2(element3, pos)



        # Inserta el elemento especificado al principio de esta lista.
        # @ param object elemento
        # @ return
    def addFirst(self, object):
        try:
            node = Node(object)
            if not self.isEmpty():
                self.Head = node
                self.Tail = node
            else:
                node.Next = self.Head
                self.Head = node
            return True
        except:
            return False


        # Inserta el elemento especificado al final de esta lista.
        # @ param object elemento
        # @ return
    def addLast(self, object):
        try:
            node = Node(object)
            if not self.isEmpty():
                self.Head = node
                self.Tail = node
            else:
                Route = self.Head
                while Route != None:
                    Route = Route.Next
                self.Tail.Next = node
                self.Tail = node
        except:
            return False


        # Elimina todos los elementos de esta lista.
    def clear(self):
        self.Head = None


        # Clona la Lista
    def clone(self):
        ListCopia = ListaEnlazada()
        cont = self.Head
        while cont:
            ListCopia.add(cont.object)
            cont = cont.Next
        print("CLON DE LA LISTA")
        ListCopia.toString()
        print("ListCopia is List:", (ListCopia is List))


        # Devuelve verdadero si contiene el elemento.
        # @ param object elemento
        # @ return
    def contains(self, element):
        cont = self.Head
        while cont:
            if cont.object == element:
                return True
            cont = cont.Next



        # Devuelve verdadero si contiene todos los elementos.
        # @ param objects elementos
        # @ return
    def containsAll(self, element1, element2, element3):
        if List.contains(element1) and List.contains(element2) and List.contains(element3):
            print("VERDADERO")


        # Devuelve el nodo del elemento especificado, o null si no contiene el elemento.
        # @ param object elemento
        # @ return
    def nodeOf(self, element):
        cont = self.Head
        Tam = 1
        while cont:
            if element == cont.object:
                print("El nodo del Elemento es el numero:", Tam)
                break
            cont = cont.Next
            Tam += 1
        else:
            print("NULL")




        # Devuelve verdadero si el objeto especificado es igual a la lista.
        # @ param object elemento
        # @ return
    def isEquals(self, object):
        if object == List:
            print("VERDADERO")


        # Obtener un elemento de la lista(depende del tipo de lista).
        # @ return
    def get(self):
        cont = self.Head
        vlr = 0
        while cont:
            if cont != None:
                vlr = cont.object
                break
            cont = cont.Next
        print(vlr)


        # Obtener un elemento de la posición del nodo especificado.
        # @ param node nodo
        # @ return
    def get2(self, element):
        cont = self.Head
        Tam = 1
        while cont and Tam != element:
            cont = cont.Next
            Tam += 1
        print(cont.object)


        # Obtener un elemento de la posición previa al nodo especificado.
        # @ param node nodo
        # @ return
    def getPrevious(self, element):
        cont = self.Head
        Prev = None
        Tam = 1
        while cont and Tam != element:
            Prev = cont.object
            cont = cont.Next
            Tam += 1
        print(Prev)


        # Obtener un elemento de la posición siguinete al nodo especificado.
        # @ param node nodo
        # @ return
    def getNext(self, element):
        cont = self.Head
        Tam = 1
        while cont and Tam != element:
            cont = cont.Next
            Tam += 1
        print(cont.Next.object)


        # Obtener el elemento especificado al principio de esta lista.
        # @ return
    def getFirst(self):
        cont = self.Head
        vlr = 0
        while cont:
            if cont != None:
                vlr = cont.object
                break
            cont = cont.Next
        print(vlr)


        # Obtner el elemento especificado al final de esta lista.
        # @ return
    def getLast(self):
        cont = self.Tail
        vlr = 0
        while cont:
            if cont != None:
                vlr = cont.object
                break
            cont = cont.Next
        print(vlr)


        # Elimina el nodo en la lista.
        # @ param object elemento
        # @ return
    def remove(self, element):
        cont = self.Head
        Prev = None
        while cont and cont.object != element:
            Prev = cont
            cont = cont.Next
        if Prev == None:
            self.Head = cont.Next
        elif cont:
            Prev.Next = cont.Next
            cont.Next = None



        # Elimina el nodo en la lista.
        # @ param node nodo
        # @ return
    def remove2(self, element):
        cont = self.Head
        Prev = None
        Tam = 1
        while cont and Tam != element:
            Prev = cont
            cont = cont.Next
            Tam += 1
        if Prev == None:
            self.Head = cont.Next
        elif cont:
            Prev.Next = cont.Next
            cont.Next = None


        # Elimina de esta lista todos sus elementos que están contenidos en la colección especificada.
        # @ param objects elementos
        # @ return
    def removeAll(self, element1, element2, element3):
        List.remove(element1)
        List.remove(element2)
        List.remove(element3)


        # Conserva solo los elementos de esta lista que están contenidos en la colección especificada.
        # @ param objects elementos
        # @ return
    def retainAll(self):
        l=1


        # Reemplaza el elemento en la posición del nodo especificado.
        # @ param node nodo
        # @ param object elemento
        # @ return
    def set(self, element, pos):
        cont = self.Head
        Pos = 1
        while cont:
            if Pos == pos:
                cont.object = element
                break
            Pos += 1
            cont = cont.Next
        else:
            print("Posicion de Nodo invalida")


        # Devuelve el número de elementos de esta lista.
        # @ return
    def size(self):
        cont = self.Head
        Tam = 0
        while cont:
            Tam += 1
            cont = cont.Next
        print("El tamaño de la Lista enlazada es de:", Tam)


        # Devuelve una vista de la parte de esta lista.
        # @ param from nodo
        # @ param to nodo
        # @ return
    def subList(self, a, b):
        cont = self.Head
        Pos = 1
        while cont:
            if Pos >= a and Pos <= b:
                print(cont.object)
            Pos += 1
            cont = cont.Next

        # Devuelve un array que contiene todos los elementos de esta lista.
        # * @ return
    def toArray(self):
        cont = self.Head
        Array = []
        while cont:
            Array.append(cont.object)
            cont = cont.Next
        print(Array)


        # Ordenar lista por ?
        # @ return
    def sort(self):
        cont = self.Head
        Array = []
        while cont:
            Array.append(cont.object)
            cont = cont.Next
        Array.sort(reverse=True)
        List.clear()
        print("LISTA ORDENADA DE MAYOR A MENOR")
        for i in Array:
            List.add(i)
        List.toString()


        # retorna un string con el contenido del nodo
        # @ return
    def toString(self):
        cont = self.Head
        while cont:
            print(cont.object)
            cont = cont.Next




if __name__ == '__main__':
    List = ListaEnlazada()
    List.addFirst(5)
    List.addLast(10)
    List.add(20)






    List.size()
    List.toArray()
    List.toString()

















