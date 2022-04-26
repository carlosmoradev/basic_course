#Conversor de monedas entre pesos colombianos y dolares - ahora con menu

menu = """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos

Ingresa la opcion correspondiente
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input('Cuantos pesos colombianos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 3931.74
    dolares = pesos / valor_dolar
    print(f"{pesos} pesos equivale a {dolares:.2f} dolares.")
elif opcion == 2:
    pesos = input('Cuantos pesos Argentinos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    print(f"{pesos} pesos Argentinos equivale a {dolares:.2f} dolares.")
elif opcion == 3:
    pesos = input('Cuantos pesos Mexicanos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    print(f"{pesos} pesos Mexicanos equivale a {dolares:.2f} dolares.")
else:
    print("Selecciona una opcion correcta")
