def run():
    usuario_valido = 'carlos'


    while True:
        nombre = input('Indique su usuario: ')
        if nombre != usuario_valido:
            print('Usuario no existe.  Intente de nuevo')
            continue
        print(f'Hola {usuario_valido}.  Cual es tu password? (pista es 50% agua)')
        password = input()
        if password == 'aguacate':
            print('Autenticacion exitosa.')
            break
    print('Proceso finalizado.')


if __name__ == '__main__':
    run()