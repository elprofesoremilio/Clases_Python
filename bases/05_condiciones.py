# Las estructuras condicionales permiten elegir entre dos o más
# bloques de código en función de que se cumpla o no una expresión lógica

# Para ejecutar o no una cosa
mayor_edad = False
edad = int(input("Introduce tu edad"))

if edad>=18:
    mayor_edad = True

print(mayor_edad)

# Para elegir entre dos cosas a ejecutar
if edad>=18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

# Con condiciones compuestas
es_amigo = True
if (mayor_edad or es_amigo):
    print("Te dejamos entrar")
else:
    print("No puedes entrar")

# Encadenando condiciones
dia_semana = 4

if dia_semana==1:
    print("Lunea")
elif dia_semana==2:
    print("Martes")
elif dia_semana==2:
    print("Miércoles")
elif dia_semana==2:
    print("Jueves")
elif dia_semana==2:
    print("Viernes")
elif dia_semana == 2:
    print("Sábado")
else:
    print("Domingo")
