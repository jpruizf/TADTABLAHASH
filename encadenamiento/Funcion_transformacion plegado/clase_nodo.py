class Nodo:
    __clave:object
    __sig:object

    def __init__(self,k):
        self.__clave = k

    def set_sig(self,nodo):
        self.__sig = nodo

    def get_sig(self):
        return self.__sig
    
    def get_clave(self):
        return self.__clave