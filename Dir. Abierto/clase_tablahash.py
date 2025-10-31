import numpy as np

class TablaHash:
    __tabla:np.ndarray

    def __init__(self,N):
        self.__tabla = np.empty(N,dtype=object)


    def insertar(self,clave,m):
        i = 0
        k = self.funcion_transformacion(clave,m)
        indice = int(k % len(self.__tabla))
        if i == 0:
            self.__tabla[indice] = k
            i+= 1
        else:
            while i in range(1,len(self.__tabla)-1):
                indice = k - i * int(indice % len(m))
                self.__tabla[indice] = k
                i+= 1
        return indice
    
    def funcion_transformacion(self,clave,m):
        return (clave % m)
    
    def buscar_clave(self,clave,m):
       i = 0
       k = self.funcion_transformacion(clave,m)
       while i < len(self.__tabla) and k != self.__tabla[i]:
        i+= 1
        if i > -1:
            return i
        else:
            return -1
           

    def mostrar_tabla(self):
        for fila,indice in enumerate(self.__tabla):
            print(f'Fila->{fila}|Clave->{indice}',end='\n')