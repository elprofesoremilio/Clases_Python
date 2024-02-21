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
edad = 12
print(edad)
nombre = "Juan"
print(nombre)

# También existen caracteres especiales de escritura
print("Buenos días.\nEsto está en otra línea.")
# Los caracteres especiales siempre empiezan por \ como
# \n que lo que hace es escribir un salto de línea
# otros caracteres especiales son
#   \t (tabulador)
#   \\ (escribe una barra)
#   \" o \' que escribe una comilla
print("Datos:\n\t- dato 1 tabulado\n\t- \"dato 2 entre comillas\"")

# Por suerte podemos componer 'frases' de texto combinando lo visto
# sin tener que escribir varios print
print("Hola me llamo",nombre,"y tengo",edad,"años.")

# Si os habéis dado cuenta después de cerrar comillas en llamo
# no hay espacio y sin embargo al escribir sí que aparece un espacio,
# eso es porque después de cada parámetro separado por coma ','
# que ponemos en print, se escribe automáticamente un espacio.
# ¿Y si no quiero que no lo haga?
print("Hola me llamo ",nombre," y tengo ",edad," años.",sep="'")

# Como puedes comprobar, el modificador 'sep' puede hacer que cambie
# lo que se escribe después de cada parámetro de print.
# Si no queremos que se escriba nada indicamos una cadena vacía
print("Hola me llamo ",nombre," y tengo ",edad," años.",sep="")

# Por defecto, si no decimos nada, print escribe al final un salto de línea
# También podemos modificar lo que queremos que se escriba al final
print ("Esto no salta de línea y escribe un punto",end=".")
print(" Esto no salta de línea y no escribe nada al final.",end="")
print(" Ahora sí que salta de línea al final.",end="\n")
print("Ahora también va a saltar con un carácter especial.\n",end="")
print("Ahora también, que es como funciona por defecto")
# Estas directivas que modifican print deben ir siempre al final,
# y ambas se pueden combinar
print("Cada","palabra","está","separada","por","asteríscos","y"
      ,"al","final","tengo","una","arroba",sep="*",end="@")
