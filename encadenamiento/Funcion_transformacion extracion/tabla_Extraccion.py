from clase_nodo import Nodo
import numpy as num
class TablaHash:
    __tabla:num.ndarray

    def __init__(self,N):
        self.__tabla= num.empty(N,dtype= Nodo)

    def funcion_transfomacion(self,clave,m):
        '''Extraccion de 10000 digitos'''
        return ((clave % m)/3)
    
    def insertar(self,clave,m):
        k = self.funcion_transfomacion(clave,m)
        indice = int(k % len(self.__tabla))
        nuevo = Nodo(k)
        nuevo.set_sig(self.__tabla[indice])
        self.__tabla[indice] = nuevo
        return k
    
    def mostrar_claves(self):
        for fila,nodo in enumerate(self.__tabla):
            print(f'Fila->{fila}')
            aux = nodo
            while aux is not None:
                print(f'Clave->{aux.get_clave()}')
                aux = aux.get_sig()

    def buscar_clave(self,clave,m):
        k = self.funcion_transfomacion(clave,m)
        indice = int(k % len(self.__tabla))
        i = 0
        while i < len(self.__tabla):
            if self.__tabla[i].get_clave() == k:
                print('encontrado')
                return k
            else:
                i+= 1
                return -1