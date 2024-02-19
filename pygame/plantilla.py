# Importar e inicializar la librería pygame
import pygame
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

# Inicializamos el reloj
reloj = pygame.time.Clock()

# GameLoop o bucle del juego, no toques nada hasta que se indique
running = True
while running:

    # Este bucle sirve para saber si se está pulsando el ratón o el teclado
    # NO TOCAR
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # TODO: A PARTIR DE AQUÍ ES DONDE ESCRIBES TU CÓDIGO

    screen.fill(BLANCO)


    # NO ESCRIBAS CÓDIGO MÁS ALLÁ DE AQUÍ
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # TODO FPS:
    #   Limitamos los fotogramas por segundo (frames per second) a la cantidad que indicamos arriba
    reloj.tick(FPS)

    # NO TOCAR
    # Esto refresca la pantalla dibujando aquello que se ha tratado de pintar
    # desde la última vez que se llamó a flip()
    pygame.display.flip()

# NO TOCAR
pygame.quit()