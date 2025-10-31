from clase_tablahash import TablaHash
import random
def test():
    N = random.randint(1,8)
    M = N/0.7
    t = TablaHash(N)
    for i in range(N):
        clave = int(input('Genere una contraseña->'))
        direccion = t.insertar(clave,M)
        print(f'Direccion de la contraseña->{direccion}',end='\n')
    resultado = t.buscar_clave(333,M)
    if resultado != -1:
        print(f'Direccion de la clave->{resultado}')
    else:
        raise UnboundLocalError('Error Direccion no encotrada')
    t.mostrar_tabla()





if __name__ == '__main__':
    test()