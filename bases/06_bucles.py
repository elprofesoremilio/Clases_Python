# Un bucle sirve para repetir una o varias instrucciones
# Existen dos tipos de bucles:
#   - Centinela: se ejecutan mientras una expresión lógica es verdadera
#   - Contador: se ejecutan un número determinado de veces en función de una expresión numérica


# Bucles centinela => while (condición) => mientras se ejecute la condición
edad = 1
print("Tengo",edad,"año")
while edad<18:
    edad = edad + 1
    print("Crezco un año, tengo:",edad,"años")

print(edad)