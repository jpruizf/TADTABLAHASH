from tabla_Extraccion import TablaHash
import random
def test():
    N= random.randrange(500)
    M= N/0.7
    t= TablaHash(N)
    t.insertar(random.randint(0,3000),M)
    t.insertar(random.randint(0,3000),M)
    t.insertar(random.randint(0,3000),M)
    t.insertar(random.randint(0,3000),M)
    t.insertar(random.randint(0,3000),M)
    t.mostrar_claves()





if __name__ == '__main__':
    test()