# Las expresiones relacionales devuelven un valor logico verdadero o falso: True False
# los operandos solo podrán ser variables o valores que pueda verse si uno es mayor que otro
# comparadores:  > >= < <= != ==
# expresión_relacional => expresion_numerica comparador expresion_numerica
mayor = 10
menor = 5
igual = 10
print(mayor < menor)
print(mayor > menor)
print(mayor == igual)
print(mayor >= igual)
print(mayor <= igual)
print(mayor != igual)
# expresion_relacional => expresion_textual comparador expresion_textual
letraA = "a"
letraB = "b"
letra_a = "a"
texto = "Ahora con mayúscula"
print(letraA == letra_a)
print(letraA < letraB)
print(letraA > letraB)
print(letraA >= letra_a)
print(letraA <= letraB)
print(letraA != letra_a)
# Ten en cuenta que podemos asignar a una variable una expresión relacional
resultado = letraA >= "Z"  # esto dará verdadero, porque las minúsculas se consideran anteriores a las mayúsculas
print(resultado)