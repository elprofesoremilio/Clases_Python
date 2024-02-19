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

# Otras configuraciones
TITLE = "Mover objetos"
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

# Definimos los datos para la bola y su movimiento
ball_radius = 20    # radio
ball_pos_x = screen.get_width()/2   # posición x inicial
ball_pos_y = 150                    # posición en y
BALL_VELOCITY = 5                   # Velocidad a la que se moverá la bola en píxeles por fotograma
ball_velocity_x = BALL_VELOCITY     # velocidad horizontal de la bola, empieza hacia la derecha
ball_velocity_y = -BALL_VELOCITY    # velocidad vertical de la bola, empieza hacia arriba

# Delta es una variable necesaria para que el juego vaya siempre bien
# independientemente de que tu PC sea más rápido o más lento
# Almacenará el tiempo que ha transcurrido entre un fotograma y otro
delta = 0

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

    # TODO: comprobar si la bola choca con algún borde
    # Si la bola sobrepasa el borde derecho le damos velocidad horizontal negativa
    if ball_pos_x > SCREEN_WIDTH-ball_radius:
        ball_velocity_x = -BALL_VELOCITY
    # Si la bola sobrepasa el borde izquierdo le damos velocidad horizontal positiva
    elif ball_pos_x < 0+ball_radius:
        ball_velocity_x = BALL_VELOCITY
    # Si la bola sobrepasa el borde superior le damos velocidad vertical negativa
    if ball_pos_y > SCREEN_HEIGHT-ball_radius:
        ball_velocity_y = -BALL_VELOCITY
    # Si la bola sobrepasa el borde inferior le damos velocidad vertical positiva
    elif ball_pos_y < 0+ball_radius:
        ball_velocity_y = BALL_VELOCITY

    # TODO: calcular nueva posición de la bola
    ball_pos_x = ball_pos_x + ball_velocity_x
    ball_pos_y = ball_pos_y + ball_velocity_y

    screen.fill(BLANCO)

    # TODO: dibujamos la bola
    pygame.draw.circle(screen,NEGRO,(ball_pos_x,ball_pos_y), ball_radius)

    # NO ESCRIBAS CÓDIGO MÁS ALLÁ DE AQUÍ
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # --- Limitamos a los fotogramas por segundo (frames per second) definidos arriba
    reloj.tick(FPS)

    # NO TOCAR
    # Esto refresca la pantalla dibujando aquello que se ha tratado de pintar
    # desde la última vez que se llamó a flip()
    pygame.display.flip()
    
# NO TOCAR
pygame.quit()