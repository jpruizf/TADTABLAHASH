from clase_nodo import Nodo
import numpy as np

class TablaHash:
    __tabla:np.ndarray
    
    def __init__(self,N):
        self.__tabla = np.empty(N,dtype=Nodo)

    def insertar(self,valor,m):
        k = self.funcion_transformacion(valor,m)
        #print('key actual->',k)
        print('key nuevo->',k)
        indice = int(k % len(self.__tabla))
        print('indice',indice)
        nodo = Nodo(k)
        nodo.set_sig(self.__tabla[indice])
        self.__tabla[indice] = nodo
        return k
    
    def funcion_transformacion(self,valor,m):
        return (valor % m)
    
    def buscar(self,clave,m):
        k = self.funcion_transformacion(clave,m)
        indice = int(k % len(self.__tabla))
        for i, nodo in enumerate(self.__tabla):
            actual = nodo
            if actual is not None and actual.get_clave() == k:
                print('encontrado')
                return actual.get_clave()
            else:
                return -1
    
    def eliminar(self,clave,m):
        k = self.funcion_transformacion(clave,m)
        encontrado = self.buscar(k,m)
        if encontrado != -1:
            indice = encontrado % len(self.__tabla)
            dato = self.__tabla[indice]
            del dato
            print('Dato eliminado')
        else:
            raise ValueError('Error! clave inconrrecta o inexistente')
    def tamanio_tabla(self):
        return len(self.__tabla)
    
    def vacio(self):
        return self.__tabla == None
    
    def mostrar_claves(self):
        for i, nodo in enumerate(self.__tabla):
            print(f'indice->{i}:',end=' ')
            aux = nodo
            while aux is not None:
                print(f'Clave->{aux.get_clave()}',end=' ')
                aux = aux.get_sig()
            print('None')