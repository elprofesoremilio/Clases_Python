# EXPRESIONES: vamos a definir las expresiones de forma recursiva y con respecto a la asignación
# Es decir, vamos a crear una variable, y lo que haya a la derecha del = será nuestra expresión
# Trabajaremos por ahora con expresiones numéricas enteras aunque la definición es extensible
# Una expresión es un literal, por lo que siempre podré asignar como valor un literal a una variable
# expresión → literal o variable
variable = 1
numero = variable
# expresión → operador_unario expresión
# los operadores unarios numéricos son + y - y se ponen delante del literal o la variable
variable = +1
numero = -variable
# Expresión -> (expresión)
variable = (-numero)
numero = (+1)
# Expresión → expresión operador_binario expresión
# Hay diversos operadores binarios numéricos:
# +
suma = 1 + 2
suma = suma + 3
# -
resta = 5 - 2
resta = 10 - resta
# // o división entera (se redondea, no se dejan decimales)
division_entera = 10 // 6   # dará como resultado 1
division_entera = 3 // division_entera
# / o división real
division_real = 10 / 6  # dará como resultado 1.666666666...7
# % operación resto, llamada normalmente módulo, devuelve el resto de dividir un número entre otro
resto = 9 % 2   # el resto de dividir 9 / 2 es 1, y ese es el resultado de esta operación
# *
multiplicar = 3 * 6
# ** operación potencia, eleva un número a otro
potencia = 2 ** 3   # eleva 2 a 3, es decir, 2*2*2 = 8
#   IMPORTANTE: si una operación numérica contiene dos enteros el resultado será un entero
#               si una operación numérica contiene al menos un real, el resultado será un real
entero = 4 + 3 - (3//2)
real = 4+3 - (3/2)
otro_real = 1.0 + 2
print(entero)
print(real)
print(otro_real)

# Ahora una operación compleja poniendo en práctica lo anterior
operacion_compleja = -(-5*3+11//5) % 5
print(operacion_compleja)
# Existe un orden al hacer las operaciones
# 1. Primero se calculan los paréntesis
# 2. Luego los operadores unarios
# 3. Después las potencias
# 4. Tras eso multiplicaciones y divisiones en el orden en que se encuentren
# 5. Finalmente, sumas y restas en el orden en que se encuentren
# Siguiendo estas normas, la operación anterior quedaría así
op1 = -5
op1 = op1*3
op2 = 11//5
por_orden = op1 + op2
por_orden = -por_orden
por_orden = por_orden % 5
print(por_orden)
# Siempre recomiendo usar paréntesis cuando existan posibles dudas
# Fíjate que después de usar los paréntesis como queremos, cambia el resultado
con_parentesis = -((-(5*3)+(11//5)) % 5)
print(con_parentesis)