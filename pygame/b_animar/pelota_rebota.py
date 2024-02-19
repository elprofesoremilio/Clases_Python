# Importar e inicializar la librería pygame
import pygame
from pygame.locals import *
pygame.init()

# TODO: definir constantes (siempre en mayúsculas)
#   Aquí podemos crear distintas variables que servirán de configuración

# Colores
# Ten en cuenta que los colores se definen por cantidad de Rojo, cantidad de Verde y cantidad de Azul.
# Las cantidades van desde el mínimo de color, 0, hasta el máximo de color, 255
# Te aconsejo escribir el nombre del color en mayúsculas, porque así es como se indica que es un valor constante
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Otras configuraciones
TITLE = "Pelota que rebota"
FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# TODO: definir la pantalla
# Inicializar el modo de dibujado indicando el tamaño de la pantalla
# Puedes modificar los píxeles del tamaño de la pantalla
# El primer parámetro es el ancho y el segundo el alto
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# TODO: Título de la ventana
pygame.display.set_caption(TITLE)

# TODO: definir variables que gestionen los objetos del juego
#   Para la pelota pelota
ball_radius = 20
ball_x = screen.get_width()/2
ball_y = 150
BALL_VELOCITY = 3
ball_velocity_x = BALL_VELOCITY
ball_velocity_y = -BALL_VELOCITY

# Inicializamos el reloj
reloj = pygame.time.Clock()

# GameLoop o bucle del juego, no toques nada hasta que se indique
running = True
while running:

    # Este bucle sirve para saber si se está pulsando el ratón o el teclado
    # NO TOCAR
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #tecla pulsada
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    if ball_x > SCREEN_WIDTH-ball_radius:
        ball_velocity_x = -BALL_VELOCITY
    elif ball_x < 0+ball_radius:
        ball_velocity_x = BALL_VELOCITY
    if ball_y > SCREEN_HEIGHT-ball_radius:
        ball_velocity_y = -BALL_VELOCITY
    elif ball_y < 0+ball_radius:
        ball_velocity_y = BALL_VELOCITY

    screen.fill(BLANCO)

    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    pygame.draw.circle(screen, NEGRO, (ball_x, ball_y), ball_radius)
    # NO ESCRIBAS CÓDIGO MÁS ALLÁ DE AQUÍ
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------



    # NO TOCAR
    reloj.tick(FPS)
    # Esto refresca la pantalla dibujando aquello que se ha tratado de pintar
    # desde la última vez que se llamó a flip()
    pygame.display.flip()
    
# NO TOCAR
pygame.quit()