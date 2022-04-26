#Conversor de monedas entre pesos colobianos y dolares

pesos = input('Cuantos pesos colombianos tienes?: ')
pesos = float(pesos)
valor_dolar = 3931.74
dolares = pesos / valor_dolar

print(f"{pesos} pesos equivale a {dolares:.2f} dolares.") # el :.2f redondea la cantidad de decimales a 2.