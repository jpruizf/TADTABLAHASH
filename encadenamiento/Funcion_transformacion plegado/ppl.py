from tabla_plegado import Tabla_Hash
import random

def test():
    N= random.randrange(50)
    M= N/0.7
    t= Tabla_Hash(N)
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    k = t.insertar(random.randint(1,90),M)
    print(f'Clave generada->{k}')
    t.mostrar_clave()


if __name__ == '__main__':
    test()