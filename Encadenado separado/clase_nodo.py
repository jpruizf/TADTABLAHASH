class Nodo:
    __clave:object
    __sig:object

    def __init__(self,c):
        self.__clave = c
        self.__sig = None

    def setSig(self,nodo):
        self.__sig = nodo

    def getSig(self):
        return self.__sig
    
    def getClave(self):
        return self.__clave