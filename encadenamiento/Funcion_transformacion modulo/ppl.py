from clase_tabla import TablaHash
import random
def test():
    tamanio = 10
    M = tamanio/0.7
    th = TablaHash(tamanio)
    th.insertar(random.randint(0,9),M)
    th.insertar(random.randint(0,6),M)
    th.insertar(random.randint(0,7),M)
    th.insertar(random.randint(0,8),M)
    #th.eliminar(2,M)
    resultado = th.buscar(8.0,M)
    print('resultado->',resultado)
    th.mostrar_claves()

if __name__ == '__main__':
    test()