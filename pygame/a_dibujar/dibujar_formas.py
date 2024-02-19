# Plantilla

# Importar e inicializar la librería pygame
import pygame
pygame.init()

# TODO: definir la pantalla
# Inicializar el modo de dibujado indicando el tamaño de la pantalla
# Puedes modificar los píxeles del tamaño de la pantalla
# El primer parámetro es el ancho y el segundo el alto
screen = pygame.display.set_mode([500, 500])

# TODO: Definir constantes (siempre en mayúsculas)
# Definimos PI para los ángulos
PI = 3.14159265
# Definimos colores: aquí puedes poner todos los colores que quieras
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
NARANJA = (200,100,0)
TURQUESA = (0,255,255)

# Otras configuraciones
TITLE = "Mi programa gráfico"
FPS = 60

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
    # A PARTIR DE AQUÍ ES DONDE ESCRIBES TU CÓDIGO

    # Cosas que puedes hacer

    # TODO: rellenar la pantalla de un color
    screen.fill(BLANCO)

    # TODO: dibujar un círculo
    # Los parámetros entre corchetes indican coordenadas x e y del centro del círculo
    # La última coordenada indica el radio
    pygame.draw.circle(screen,VIOLETA,[350,250], 50)

    # TODO: Dibujar una elipse.
    # Las coordenadas indican posición x e y del centro, radio1 y radio 2
    # Si igualas los radios dibujarás un círculo
    pygame.draw.ellipse(screen, AMARILLO, [100, 50, 200, 100])

    # Si añades al final un número solo dibujará un borde.
    # El número que indicas es el ancho de ese borde
    pygame.draw.ellipse(screen, AZUL, [90, 150, 210, 110],10)

    # TODO: dibujar un rectángulo
    # Los números que deben ir entre corchetes indican:
    # Posición en x,y del punto inicial del rectángulo, ancho y alto
    pygame.draw.rect(screen, VERDE, [0, 350, 500, 150])

    # TODO: líneas individuales
    # Esto dibuja una línea
    # Las coordenadas entre corchetes indican:
    # x, y del punto inicial de la línea
    # x, y del punto final de la línea
    # ancho de la línea
    pygame.draw.line(screen, NEGRO, [50,400], [400,450], 3)

    # TODO: Dibujar un polígono
    # En realidad lo que dibujamos es un polígono
    # Lo que hacemos es indicarle las coordenadas x,y de cada punto del polígono
    # Lo siguiente dibuja un triángulo, indicamos cada punto por separado
    pygame.draw.polygon(screen, ROJO, [[300, 150], [450, 150], [375, 50]])
    # Prueba a añadir más puntos
    # Fíjate bien en cómo están los corchetes

    # Por otro lado, puedes dibujar también sólo el borde del polígono con el siguiente método
    # Aparte del nombre del método hay que indicar, en el tercer parámetro (closed) si queremos
    # que el polígono quede cerrado (True) o abierto (False)
    pygame.draw.lines(screen, NEGRO, True, [[280, 170], [470, 170], [375, 40]])

    # TODO: dibujar un arco
    # Los parámetros del método son: superficie, color, rectángulo de la elipse, ángulo inicial, ángulo final
    # El rectángulo se representa [x, y, ancho, alto]
    # Los ángulos se representan en radianes, teniendo siempre como referencia PI definido arriba
    # Al final podemos poner opcionalmente el ancho del arco en píxeles
    pygame.draw.arc(screen,TURQUESA,(100,300,150,100),PI/2,3*PI/2,5)

    # NO ESCRIBAS CÓDIGO MÁS ALLÁ DE AQUÍ
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