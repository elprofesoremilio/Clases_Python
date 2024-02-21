# Una variable es como una caja donde guardamos algo
# A cada caja que creamos debemos darle un nombre

# Para crear una variable hay que escribir su nombre y darle valor con =
# El formato es: nombre_variable = literal
# Se considera un literal un valor fijo, invariable, escrito de una forma concreta
numero = 12  # Literal 12, es un número entero
nombre = "Juan"  # Literal "Juan", escrito entre comillas, indica que es un texto

# Existen 6 tipos de valores posibles que se asignan en función del valor asignado
# A continuación hay ejemplos de cómo declarar los distintos tipos y sus posibles literales
# # ENTERO → int → números enteros
entero = 1
# # REAL -> float -> números reales (con decimales . y exponenciales e10)
real = 1.3e3
otro_real = 1.3
otro_real_mas = 1e10
# # STRING o TEXTO → str -≥ siempre deben estar entre comillas
texto = "Esto es un texto entre comillas dobles"
otro_texto = 'También puede ir entre comillas simples'
# Aquí el valor literal no es 23, es "23", quiere decir que es un texto
# Nunca será tratado como un número a no ser que hagamos algo al respecto
texto_final = "23"
# # BOOLEAN o LÓGICO -> bool -> True o False
logico_verdadero = True
logico_falso = False

# # Existen dos valores especiales más, que son listas y tuplas y que ya veremos posteriormente

# En algunos casos podemos pasar de un tipo a otro usando funciones
# CUIDADO: si tratamos de convertir datos incompatibles terminará el programa con una excepción
#   pasar a entero
entero1 = int("13")
entero2 = int(1.3)
#   pasar a float
real1 = float(entero)
real2 = float("2.5")
#   pasar a texto
texto1 = str(entero1)
texto2 = str(real1)
texto3 = str(True)
#   pasar a lógico (booleano)
logico1 = bool(entero)
logico2 = bool("False")
