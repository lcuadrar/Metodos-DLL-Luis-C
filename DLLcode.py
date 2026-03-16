class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  
        self.anterior = None   

class ListaDoble:
    def __init__(self):
        self.cabeza = None  

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo  
        else:
            nuevo.siguiente = self.cabeza  
            self.cabeza.anterior = nuevo   
            self.cabeza = nuevo            

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo  
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente  
            actual.siguiente = nuevo      
            nuevo.anterior = actual       

    def insertar_posicion(self, dato, pos):
        if pos <= 1:
            self.insertar_inicio(dato) 
            return
        nuevo = Nodo(dato)
        actual = self.cabeza
        i = 1
        while actual and i < pos-1:
            actual = actual.siguiente 
            i += 1
        if actual is None:
            self.insertar_final(dato) 
        else:
            siguiente = actual.siguiente
            nuevo.siguiente = siguiente   
            nuevo.anterior = actual       
            actual.siguiente = nuevo      
            if siguiente:
                siguiente.anterior = nuevo  

    def insertar_despues(self, dato, buscar):
        actual = self.cabeza
        while actual:
            if actual.dato == buscar:
                nuevo = Nodo(dato)
                siguiente = actual.siguiente
                nuevo.siguiente = siguiente   
                nuevo.anterior = actual       
                actual.siguiente = nuevo      
                if siguiente:
                    siguiente.anterior = nuevo  
                return
            actual = actual.siguiente
        print("Elemento a buscar no encontrado.") 

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("Lista vacía")
            return
        while actual:
            print(actual.dato, end="-->")  
            actual = actual.siguiente
        print("None")  

    def mostrar_inversa(self):
        actual = self.cabeza
        if actual is None:
            print("Lista vacía")
            return
        while actual.siguiente:
            actual = actual.siguiente  
        while actual:
            print(actual.dato, end="<--")  
            actual = actual.anterior
        print("None")  

    def eliminar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente  
                else:
                    self.cabeza = actual.siguiente  
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior  
                return
            actual = actual.siguiente
        print("Elemento no encontrado.") 

    def modificar_posicion(self, pos, nuevo_valor):
        actual = self.cabeza
        i = 1
        while actual and i < pos:
            actual = actual.siguiente  
            i += 1
        if actual:
            actual.dato = nuevo_valor  
        else:
            print("Posición fuera de rango") 

    def ordenar_menor_mayor(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.dato > siguiente.dato:
                    actual.dato, siguiente.dato = siguiente.dato, actual.dato  
                siguiente = siguiente.siguiente
            actual = actual.siguiente  

    def ordenar_mayor_menor(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            while siguiente:
                if actual.dato < siguiente.dato:
                    actual.dato, siguiente.dato = siguiente.dato, actual.dato  
                siguiente = siguiente.siguiente
            actual = actual.siguiente
          
    def sumar_nodos(self):
        total = 0
        actual = self.cabeza
        while actual:
            total += actual.dato  
            actual = actual.siguiente
        return total
        

lista = ListaDoble()

lista.insertar_inicio(5)
lista.insertar_inicio(2)
lista.insertar_final(10)
lista.insertar_final(15)
lista.insertar_final(18)
lista.insertar_posicion(12, 4)
lista.insertar_despues(20, 10)
lista.insertar_despues(25, 18)

print("Lista normal:")
lista.mostrar()
print("Lista inversa:")
lista.mostrar_inversa()

lista.modificar_posicion(2, 7)
lista.modificar_posicion(5, 17)
print("Después de modificar posiciones 2 y 5:")
lista.mostrar()

lista.ordenar_menor_mayor()
print("Ordenar de menor a mayor:")
lista.mostrar()

lista.ordenar_mayor_menor()
print("Ordenar de mayor a menor:")
lista.mostrar()

print("Suma de todos los nodos:", lista.sumar_nodos())

lista.eliminar(12)
lista.eliminar(25)
print("Después de eliminar 12 y 25:")
lista.mostrar()
