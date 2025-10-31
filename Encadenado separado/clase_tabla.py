from clase_nodo import Nodo
import numpy as np
class Tabla:
    __tab:np.ndarray
    __cabeza:Nodo

    def __init__(self, tamanio):
        self.__tab = np.empty(tamanio,dtype=Nodo)
        self.__cabeza = None

    def insertar(self,valor,m):
        k = self.convertir_clave(valor,m)
        indice = int(k % len(self.__tab))
        nodo = Nodo(k)
        nodo.setSig(self.__tab[indice])
        self.__tab[indice] = nodo
        self.__cabeza = nodo
        return k
    
    def convertir_clave(self,valor,m):
        return (valor % m)

    def buscar(self,k):
       indice = int(k % len(self.__tab))
       return self.__tab[indice]
        

    def mostrar_claves(self):
        for i, nodo in enumerate(self.__tab):
            print(f'indice->{i}:', end=' ')
            actual = nodo
            while actual is not None:
                print(f'{actual.getClave()}->', end=' ')
                actual = actual.getSig()
            print('None')