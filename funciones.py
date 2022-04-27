#Practica inicial con funciones.

def conversacion(eleccion):
    print(f"Hola.  Como estas? has seleccionado el el numero {eleccion}.  Adios")

opcion = int(input('Elige una opcion (1, 2, 3): '))
if opcion == 1:
    conversacion(opcion)
elif opcion == 2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print("Elije una opcion valida")

