# FUNCIONES
# Las funciones son trozos de código que podemos usar simplemente
# llamando al nombre de la función. Si algún código lo vamos a usar
# muchas veces, podemos crear una función con ese código y no tener
# que escribirlo más. Por ejemplo, escribir por pantalla.
print("Hola caracola.")

# Existe muchas FUNCIONES predefinidas, como las que se han explicado en bases
# para la conversión de tipos: int(), str(), bool(), float()
# o como la que hemos visto para imprimir por pantalla
# Fíjate en cómo el nombre de la función lleva siempre detrás unos paréntesis ()
# Esos paréntesis pueden estar rellenos de argumentos/parámetros, que son
# datos que pasamos a la función para que pueda funcionar
print("Detro de print ponemos lo que queremos escribir")
# aunque a veces algunas funciones no necesitan parámetros
print() # si lo dejamos así escribe solo una línea vacía
# A print le podemos, como hemos visto, no dar ningún parámetro y
# dar un parámetro textual (entre comillas simples o dobles)
# Pero podemos pasarle todos los tipos de datos existentes
print(1)
print(1.3e1)
print(True)
# Y también variables de cualquier tipo
entero = 1
print(entero)
texto = "Hola"
print(texto)




#escribir Hola me llamo Juan, tengo 12 años
print("Hola me llamo",nombre,"y tengo",numero,"años.")

#Si os habéis dado cuenta después de llamo no hay espacio
#y sin embargo al escribir pone un espacio, eso es porque
#después de cada coma ',' que ponemos en print, se pone
#automáticamente un espacio. ¿Y si no quiero que no lo haga?
print("Hola me llamo ",nombre," y tengo ",numero," años.",sep="'")

#Para leer de teclado: input devuelve el texto que escribamos
#hasta que pulsemos ENTER
nombre = input("Escribe tu nombre: ")

#Si leemos números debemos convertirlos de texto a número
numero = int(input("Escribe tu edad: "))

print(nombre)
print(numero)

if numero>=18:
    print(nombre,", puedes sacarte el carné.",sep="")
else:
    años_que_faltan = 18 - numero
    print(nombre,", tienes que esperar ",años_que_faltan," años.", sep="")

