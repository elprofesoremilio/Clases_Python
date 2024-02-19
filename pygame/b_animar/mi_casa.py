"""
 Base para un archivo pygame
"""
import math

import pygame

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
AMARILLO = (255, 255, 0)

nube_x = 500
nube_y = 75
nube_variacion = 25
nube_velocidad = 0.1
nube_contador = 0
nube_limite = 200

cielo_color = [0, 0, 100]
cielo_variacion = 150
cielo_contador = 0
cielo_velocidad = 1

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi programa gráfico")

# El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.

hecho = False

# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    if cielo_contador > cielo_variacion:
        cielo_velocidad = -1
    elif cielo_contador <= 0:
        cielo_velocidad = 1


    cielo_contador += cielo_velocidad

    cielo_color[1] += cielo_velocidad
    cielo_color[2] += cielo_velocidad

    if nube_contador > nube_limite or nube_contador < 0:
        nube_velocidad = -nube_velocidad
    if nube_velocidad > 0:
        nube_contador += 1
    else:
        nube_contador -= 1;

    nube_x = nube_x + nube_velocidad

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(cielo_color)

    # Dibujamos un círculo, el sol
    pygame.draw.ellipse(pantalla, AMARILLO, [510, 50, 50, 50])
    # y las nubes
    pygame.draw.ellipse(pantalla, BLANCO, [nube_x - nube_variacion, nube_y, 50, 50])
    pygame.draw.ellipse(pantalla, BLANCO, [nube_x, nube_y + nube_variacion, 50, 50])
    pygame.draw.ellipse(pantalla, BLANCO, [nube_x + nube_variacion, nube_y, 50, 50])

    # Dibujamos un rectángulo, empezando [coordenada_x, coordenada_y, ancho, alto]
    pygame.draw.rect(pantalla, BLANCO, [250, 150, 200, 200])
    pygame.draw.rect(pantalla, VERDE, [0, 350, 700, 150])
    pygame.draw.rect(pantalla, NEGRO, [350, 250, 50, 100])
    pygame.draw.rect(pantalla, AZUL, [275, 200, 50, 50])

    # Esto dibuja un triángulo, indicamos cada punto por separado
    pygame.draw.polygon(pantalla, ROJO, [[250, 150], [450, 150], [350, 50]])

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
