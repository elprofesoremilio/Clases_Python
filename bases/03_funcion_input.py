# Existen funciones que además de ejecutar su código, también nos dan un resultado
# Ese resultado se puede asignar a una variable o utilizar como parámetro de otra función

# FUNCIÓN input
# Sirve para obtener datos desde el teclado: input devuelve el texto que escribamos
# hasta que pulsemos ENTER.
input()
# En el caso anterior, por un lado la pantalla se queda esperando pero
# nosotros podemos no saber que hacer porque no se nos dan instrucciones
# Por otro lado el texto se pierde porque no lo guardamos
# Si no queremos que este texto se pierda, lo debemos guardar en una variable
nombre = input("Escribe tu nombre: ")
# Como ves podemos también indicar un texto que se escribirá al solicitar el dato

# Ten en cuenta que input siempre devuelve texto (string)
# Si queremos leer números deberemos convertirlos con las funciones que vimos
edad = input("Escribe tu edad: ")
edad = int(edad) # fíjate cómo cambiamos el tipo de la variable sin problemas

# También podemos hacer el cambio directamente
numero = int(input("Escribe tu número favorito: "))
# En este caso, input devuelve un valor que se utiliza como parámetro para int
# que a su vez devuelve el resultado de convertir el texto de input a entero

# Para finalizar, lo escribimos junto de una forma nueva, en la que poniendo
# una f al principio del parámetro de print podemos juntar texto y variables como sigue:
print(f"Nombre: {nombre}\nEdad: {edad}\nNúmero favorito: {numero}")
