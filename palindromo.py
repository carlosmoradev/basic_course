def palindromo(palabra):
    palabra = palabra.lower().replace(' ', '')
    if palabra == palabra[::-1]:
        return True


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    print("El resultado es: ", 'Correcto' if es_palindromo else 'Fallido')


if __name__ == '__main__':
    run()