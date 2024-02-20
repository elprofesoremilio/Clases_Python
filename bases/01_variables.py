# Una variables es como una caja donde guardamos algo
# A cada caja que creamos debemos darle un nombre

# Para crear una variable hay que escribir su nombre y darle valor con =
numero = 12
nombre = "Juan"

# Existen 6 tipos de valores posibles que se asignan en función del valor asignado
#   int --> números enteros
entero = 1
#   float --> números reales (con decimales . y exponenciales e10)
real = 1.3e3
otro_real = 1.3
otro_real_mas = 1e10
#   texto --> siempre deben estar entre comillas
texto = "Esto es un texto entre comillas dobles"
otro_texto = 'También puede ir entre comillas simples'
#   lógico --> True o False
logico_verdadero = True
logico_falso = False
#   listas y tuplas --> las veremos posteriormente

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

