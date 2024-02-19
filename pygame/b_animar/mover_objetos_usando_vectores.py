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
ball_pos = pygame.Vector2(screen.get_width()/2, 150)    # posición, en este caso un vector
BALL_VELOCITY = 150     # Velocidad a la que se moverá la bola
ball_velocity = pygame.Vector2(BALL_VELOCITY, -BALL_VELOCITY)   # vector de velocidad

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
    if ball_pos.x > SCREEN_WIDTH-ball_radius:
        ball_velocity.x = -BALL_VELOCITY
    # Si la bola sobrepasa el borde izquierdo le damos velocidad horizontal positiva
    elif ball_pos.x < 0+ball_radius:
        ball_velocity.x = BALL_VELOCITY
    # Si la bola sobrepasa el borde superior le damos velocidad vertical negativa
    if ball_pos.y > SCREEN_HEIGHT-ball_radius:
        ball_velocity.y = -BALL_VELOCITY
    # Si la bola sobrepasa el borde inferior le damos velocidad vertical positiva
    elif ball_pos.y < 0+ball_radius:
        ball_velocity.y = BALL_VELOCITY

    # TODO: calcular nueva posición de la bola
    # El método elementwise sirve para hacer operaciones con vectores, coordenada a coordenada
    # Sumar vector (x1, y1) con vector (x2, y2) = (x1+x2, y1+y2)
    # Primero calculamos la multiplicación del vector de velocidad por delta, para ajustar el movimiento
    # a ball_velocity píxeles por segundo
    velocity_vector = ball_velocity.elementwise() * pygame.Vector2(delta,delta)
    # Después sumamos a la posición de la bola el vector de velocidad para que cada coordenada
    # avance en la dirección marcada por la velocidad
    ball_pos = ball_pos.elementwise() + velocity_vector

    screen.fill(BLANCO)

    # TODO: dibujamos la bola
    pygame.draw.circle(screen,NEGRO,(ball_pos.x,ball_pos.y), ball_radius)

    # NO ESCRIBAS CÓDIGO MÁS ALLÁ DE AQUÍ
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # TODO: calcular delta
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