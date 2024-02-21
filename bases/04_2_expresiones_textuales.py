# Como has visto con print, a veces podemos componer textos
# Esto también podemos hacerlo directamente sobre variables
nombre = "Juan"
edad = 12

# Fíjate como con las dos variables anteriores creamos un texto único
texto = "Tu nombre es " + nombre + " y tienes " + str(edad) + " años"
# También date cuenta de que hemos tenido que convertir el entero a texto con str
# Ahora podemos escribirlo completo
print(texto)
# Este texto lo hemos creado mediante una 'expresión' que trabaja con texto/cadenas/string
# La expresión es la parte a la derecha del =
# Podemos usar una expresión en cualquier sitio que pueda recibir un valor del mismo tipo
print("Tu nombre es " + nombre + " y tienes " + str(edad) + " años")
# El símbolo + con cadenas trabaja concatenando, es decir,
# añadiendo un texto al final de otro.
# Más operadores con string
# * multiplicación -> concatena la misma cadena tantas veces como indiquemos con el multiplicador
mensaje = "Hola " * 3
print(mensaje)
# Hemos visto el operador + que sirve para concatenar/añadir texto a una cadena
# Todos los operadores tienen una forma simplificada
mensaje += "Mundo. "
print(mensaje)
mensaje *= 5
print(mensaje)

# Vamos con las expresiones textuales y las definiremos parecido a las numéricas
# expresion_textual => literal_textual o variable_textual
# expresion_textual => expresion_textual operador_textual expresion_textual
print("Hola " * 3 + " esto es una expresión textual " + mensaje)
# Recuerda, cuando mezcles literales con variables no olvides siempre abrir y cerrar las comillas con los literales
