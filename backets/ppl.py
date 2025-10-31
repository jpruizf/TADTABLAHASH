from clase_buckets import Buckets
import random
def test():
    N = 3
    M = N/0.7
    b = Buckets(N)
    k= b.insertar(238745,M)
    print('Clave generada->',k)
    k= b.insertar(6746442345,M)
    print('Clave generada->',k)
    k= b.insertar(16554563,M)
    print('Clave generada->',k)
    b.mostrar_claves()
    resultado = b.buscar(238745,M)
    if resultado == -1:
        raise ValueError('Usuario no registrado')
    else:
        print(f'Usuario registrado! con clave->{resultado}')

if __name__ == '__main__':
    test()