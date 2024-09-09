import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cargar fuentes
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Variables de juego
puntuacion = 0
preguntas_restantes = 5  # Número de preguntas por nivel

# Función para mostrar texto
def mostrar_texto(texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = (x, y)
    screen.blit(superficie, rect)

# Generar una pregunta de multiplicación (Nivel 1)
def generar_pregunta():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    resultado_correcto = num1 * num2
    respuestas = [resultado_correcto, random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    random.shuffle(respuestas)
    return num1, num2, resultado_correcto, respuestas

# Nivel 1 - Tablas de multiplicar
def nivel_1():
    global puntuacion, preguntas_restantes
    while preguntas_restantes > 0:
        screen.fill(WHITE)

        # Generar una pregunta
        num1, num2, resultado_correcto, respuestas = generar_pregunta()

        # Mostrar la pregunta
        mostrar_texto(f'{num1} x {num2} = ?', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        # Mostrar las respuestas múltiples
        for i, respuesta in enumerate(respuestas):
            mostrar_texto(str(respuesta), small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50)

        # Manejar eventos de selección de respuesta
        respuesta_seleccionada = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Detectar la respuesta seleccionada según la posición del clic
                if SCREEN_HEIGHT // 2 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 50:
                    respuesta_seleccionada = respuestas[0]
                elif SCREEN_HEIGHT // 2 + 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 100:
                    respuesta_seleccionada = respuestas[1]
                elif SCREEN_HEIGHT // 2 + 100 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 150:
                    respuesta_seleccionada = respuestas[2]
                elif SCREEN_HEIGHT // 2 + 150 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 200:
                    respuesta_seleccionada = respuestas[3]

        # Comprobar la respuesta seleccionada
        if respuesta_seleccionada is not None:
            if respuesta_seleccionada == resultado_correcto:
                puntuacion += 1
                mostrar_texto('Correcto!', font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)
            else:
                mostrar_texto(f'Incorrecto! {num1} x {num2} = {resultado_correcto}', font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)

            pygame.display.update()
            pygame.time.wait(2000)
            preguntas_restantes -= 1

        pygame.display.update()

    # Mostrar la puntuación final
    mostrar_texto(f'Puntuación final: {puntuacion}', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)
    pygame.display.update()
    pygame.time.wait(3000)
    # Aquí puedes volver al mapa de niveles o avanzar al siguiente nivel

# Placeholder para los siguientes niveles
def nivel_2():
    pass

def nivel_3():
    pass
