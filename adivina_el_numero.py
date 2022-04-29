import random


def run():
    numero_aletaorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero: "))
    while numero_elegido != numero_aletaorio:
        if numero_elegido < numero_aletaorio:
            print("busca un numero mas grande!")
        else:
            print("Busca un numero mas pequeno!")
        numero_elegido = int(input("Elige otro numero: "))
    print("Ganaste!!!")


if __name__ == '__main__':
    run()
