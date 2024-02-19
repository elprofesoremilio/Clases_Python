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
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
AMARILLO = (255,255,0)

# Otras configuraciones
TITLE = "Mi programa gráfico"
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
# primero los que se encargan de gestionar al jugador
player_height = 20
player_width = 100
player_pos = pygame.Vector2(screen.get_width() / 2 - player_width/2, screen.get_height() - player_height - 50)
player_velocity = 300

# esta es necesaria para que el juego vaya siempre bien independientemente de que tu PC sea más rápido o más lento
delta = 0

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
    # TODO: Gestionar movimiento con ratón

    mouse = pygame.mouse.get_pressed()

    if (mouse[0]):
        player_pos.x = pygame.mouse.get_pos()[0]

    screen.fill(BLANCO)

    pygame.draw.rect(screen, NEGRO, [player_pos.x, player_pos.y, player_width, player_height])

    # NO ESCRIBAS CÓDIGO MÁS ALLÁ DE AQUÍ
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    # Además, guardamos delta que son los milisegundos que han pasado
    # desde que se pintó por última vez
    delta = reloj.tick(FPS) / 1000

    # NO TOCAR
    # Esto refresca la pantalla dibujando aquello que se ha tratado de pintar
    # desde la última vez que se llamó a flip()
    pygame.display.flip()
    
# NO TOCAR
pygame.quit()