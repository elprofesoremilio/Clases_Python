# Crear una lista con datos
lista = [1, 2, 3, 8]
print(lista)

# Crear una lista vacía
notas = []

# Rellenar una lista desde teclado
nota = None
while True:
    entrada = input("Ingrese una nota (o 'fin' para terminar): ")

    if entrada.lower() == 'fin':
        break  # Sale del bucle si se ingresa 'fin'

    if not entrada.isdecimal():
        print("Por favor, introduzca un número válido o 'fin'.")
    else:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("La nota debe estar entre 0 y 10.")
    # try:
    #     numero = float(entrada)
    #     notas.append(numero)
    # except ValueError:
    #     print("Por favor, ingrese un número válido o 'fin'.")

print("Lista de notas:", notas)

# Para acceder a una nota concreta se indica la posición entre corchetes
# lista[índice]
# OJO: Ten en cuenta que la primera posición siempre es la posición 0
# La función len(lista) nos dice la longitud de la lista, es decir cuántos elementos tiene
if len(notas) > 0:      # Comprueba que al menos se ha introducido una nota
    print(notas[0])     # Escribe la primera nota
