from clase_tabla import Tabla

def test():
    tamanio = int(input('Ingrese la cantidad de datos->'))
    m = tamanio/0.7
    t = Tabla(tamanio)
    valor = int(input('Ingrese numero de registro->'))
    clave = t.insertar(valor,m)
    print(f'Clave generada->{clave}')
    t.mostrar_claves()
    resultado = t.buscar(clave)
    print(f'Resultado->{resultado.getClave()}')


if __name__ == '__main__':
    test()