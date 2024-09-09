import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla para Raspberry Pi (800x480)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cargar fuentes
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 36)

# Variables de juego
puntuacion = 0
preguntas_restantes = 12  # 12 preguntas por tabla de multiplicar
tabla_seleccionada = None  # Variable para guardar la tabla de multiplicar seleccionada

# Función para mostrar texto
def mostrar_texto(texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = (x, y)
    screen.blit(superficie, rect)

# Menú para seleccionar la tabla de multiplicar (2 al 12)
def menu_tabla_multiplicar():
    global tabla_seleccionada
    while True:
        screen.fill(WHITE)
        mostrar_texto('Selecciona la tabla de multiplicar:', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)

        # Mostrar opciones de tablas (2 al 12)
        for i in range(2, 13):
            mostrar_texto(f'Tabla del {i}', small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + (i - 2) * 30)

        # Manejar eventos de selección de tabla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(2, 13):
                    if SCREEN_HEIGHT // 2 + (i - 2) * 30 - 15 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + (i - 2) * 30 + 15:
                        tabla_seleccionada = i
                        return  # Salimos del menú y pasamos al nivel

        pygame.display.update()

# Generar una pregunta de multiplicación aleatoria basada en la tabla seleccionada
def generar_pregunta():
    global tabla_seleccionada
    if tabla_seleccionada is None:
        print("Error: No se ha seleccionado ninguna tabla.")
        return None, None, None, None
    
    num1 = tabla_seleccionada
    num2 = random.randint(1, 12)  # Multiplicamos del 1 al 12 de forma aleatoria
    resultado_correcto = num1 * num2
    respuestas = [resultado_correcto, random.randint(1, 144), random.randint(1, 144), random.randint(1, 144)]  # Respuestas aleatorias
    random.shuffle(respuestas)
    return num1, num2, resultado_correcto, respuestas

# Función para dibujar los botones "Siguiente" y "Salir"
def dibujar_botones():
    # Dibujar botón "Siguiente"
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH - 180, SCREEN_HEIGHT - 80, 160, 50))
    mostrar_texto('Siguiente', small_font, WHITE, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 55)

    # Dibujar botón "Salir"
    pygame.draw.rect(screen, RED, (20, SCREEN_HEIGHT - 80, 160, 50))
    mostrar_texto('Salir', small_font, WHITE, 100, SCREEN_HEIGHT - 55)

# Nivel 1 - Tablas de multiplicar
def nivel_1():
    global puntuacion, preguntas_restantes
    preguntas_restantes = 12  # 12 preguntas por tabla
    puntuacion = 0  # Reiniciar puntuación

    # Llamar al menú de selección de tabla antes de empezar
    menu_tabla_multiplicar()

    while preguntas_restantes > 0:
        screen.fill(WHITE)

        # Generar una pregunta aleatoria
        num1, num2, resultado_correcto, respuestas = generar_pregunta()

        if num1 is None:  # Si no se seleccionó ninguna tabla, terminamos
            break

        # Mostrar la pregunta
        mostrar_texto(f'{num1} x {num2} = ?', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        # Mostrar las respuestas en dos columnas
        mostrar_texto(str(respuestas[0]), small_font, BLACK, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2)
        mostrar_texto(str(respuestas[1]), small_font, BLACK, SCREEN_WIDTH * 2 // 3, SCREEN_HEIGHT // 2)
        mostrar_texto(str(respuestas[2]), small_font, BLACK, SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 50)
        mostrar_texto(str(respuestas[3]), small_font, BLACK, SCREEN_WIDTH * 2 // 3, SCREEN_HEIGHT // 2 + 50)

        # Dibujar los botones de control
        dibujar_botones()

        # Manejar eventos de selección de respuesta y botones
        respuesta_seleccionada = None
        resultado_mostrado = False
        while not resultado_mostrado:  # Este bucle permite quedarse en la pregunta hasta que se elija "Siguiente"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Detectar la respuesta seleccionada según la posición del clic
                    if SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 - 25 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 25:
                        respuesta_seleccionada = respuestas[0]
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 - 25 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 25:
                        respuesta_seleccionada = respuestas[1]
                    elif SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 + 50 - 25 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 50 + 25:
                        respuesta_seleccionada = respuestas[2]
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 + 50 - 25 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 50 + 25:
                        respuesta_seleccionada = respuestas[3]

                    # Comprobar si se hace clic en el botón "Siguiente"
                    if SCREEN_WIDTH - 180 <= mouse_pos[0] <= SCREEN_WIDTH - 20 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        resultado_mostrado = True  # Salir del bucle cuando se presiona "Siguiente"

                    # Comprobar si se hace clic en el botón "Salir"
                    if 20 <= mouse_pos[0] <= 180 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        return  # Regresar al menú de selección de tablas

            # Mostrar si la respuesta es correcta o incorrecta
            if respuesta_seleccionada is not None:
                if respuesta_seleccionada == resultado_correcto:
                    mostrar_texto('Correcto!', font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)
                else:
                    mostrar_texto(f'Incorrecto! {num1} x {num2} = {resultado_correcto}', font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)

            pygame.display.update()

        preguntas_restantes -= 1

    # Mostrar la puntuación final
    screen.fill(WHITE)
    mostrar_texto(f'Puntuación final: {puntuacion}', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.update()
    pygame.time.wait(3000)

    # Volver al mapa de niveles después de completar el nivel 1
    mapa_niveles()

# Placeholder para los siguientes niveles
def nivel_2():
    pass

def nivel_3():
    pass
