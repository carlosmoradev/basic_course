#Conversor de monedas entre pesos colombianos y dolares - ahora con menu

def conversor(moneda, valor_dolar):
        pesos = float(input(f'Cuantos {moneda} tienes?: '))
        dolares = pesos / valor_dolar
        print(f"${int(pesos)} {moneda} pesos equivale a ${dolares:.2f} dolares.")

menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos

Ingresa la opcion correspondiente
"""

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3975)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Selecciona una opcion correcta")
