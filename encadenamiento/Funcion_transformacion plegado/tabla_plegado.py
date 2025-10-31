from clase_nodo import Nodo
import numpy as np
class Tabla_Hash:
    __tabla:np.ndarray

    def __init__(self,N):
        self.__tabla= np.empty(N,dtype=object)

    def funcion_transformacion(self,clave,m):
        return ((clave % m)+clave)
    
    def insertar(self,clave,m):
        k= self.funcion_transformacion(clave,m)
        indice= int(k % len(self.__tabla))
        nodo= Nodo(k)
        nodo.set_sig(self.__tabla[indice])
        self.__tabla[indice]= nodo
        return k
    
    def mostrar_clave(self):
        for fila,nodo in enumerate(self.__tabla):
            print(f'Fila->{fila}')
            aux = nodo
            while aux is not None:
                print(f'Clave->{aux.get_clave()}',end=' ')
                aux = aux.get_sig()
            print('None')