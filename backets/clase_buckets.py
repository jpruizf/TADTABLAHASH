import numpy as np

class Buckets:
    __cubo:np.ndarray

    def __init__(self,N):
        self.__cubo = np.empty(N,dtype=object)

    
    def insertar(self,valor,m):
        k= self.funcion_transformacion(valor,m)
        indice= int(k % len(self.__cubo))
        if self.__cubo[indice] != k:
            self.__cubo[indice]= k
        else:
            raise IndexError('Error! Key ya indexado')
        return k


    def funcion_transformacion(self,valor,m):
        return valor % m
    
    def mostrar_claves(self):
        for fila,i in enumerate(self.__cubo):
            print(f'Fila->{fila}|Componenetes->',i)

    def buscar(self,valor,m):
        k= self.funcion_transformacion(valor,m)
        bandera = False
        i = 0
        while not bandera and i < len(self.__cubo):
            if k == self.__cubo[i]:
                aux = self.__cubo[i]
                bandera = True
            else:
                i+= 1
        if bandera and aux == k:
            return aux
        else:
            return -1