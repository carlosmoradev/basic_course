#Identificar si el numero ingresado es primo
def es_primo(numero):
    if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        return True


def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("No es primo.")
    else:
        print("Es primo")


if __name__ == '__main__':
    run()

