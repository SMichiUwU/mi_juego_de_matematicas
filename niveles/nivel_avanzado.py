import pygame
import random
from compartido import mostrar_texto_centrado

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(r'fuentes/GamestationCond.otf', 50)
small_font = pygame.font.Font(r'fuentes/GamestationCond.otf', 24)
fondo_pregunta = pygame.image.load(r'imagenes/fondo_preguntas.png')
fondo_pregunta = pygame.transform.scale(fondo_pregunta, (SCREEN_WIDTH, SCREEN_HEIGHT))

def generar_pregunta():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operador = random.choice(["*", "/"])
    if operador == "*":
        resultado_correcto = num1 * num2
    else:
        resultado_correcto = num1 // num2  # Asegurarse de que la división sea entera
    respuestas = [resultado_correcto, random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    random.shuffle(respuestas)
    return num1, num2, operador, resultado_correcto, respuestas

def nivel_avanzado(screen, volver_al_mapa):
    preguntas_restantes = 12

    while preguntas_restantes > 0:
        screen.blit(fondo_pregunta, (0, 0))
        num1, num2, operador, resultado_correcto, respuestas = generar_pregunta()

        # Mostrar la pregunta y respuestas
        mostrar_texto_centrado(f'{num1} {operador} {num2} = ?', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 4, 200, 50), screen)
        mostrar_texto_centrado(str(respuestas[0]), small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[1]), small_font, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[2]), small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 + 50, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[3]), small_font, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 + 50, 100, 50), screen)
        
        pygame.display.update()
        preguntas_restantes -= 1

    volver_al_mapa()
