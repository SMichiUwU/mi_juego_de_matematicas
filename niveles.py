import pygame
import sys
import random
from compartido import mostrar_texto_centrado  # Importamos la función compartida desde el archivo compartido.py

# Inicializar Pygame
pygame.init()

# Configuración de pantalla para Raspberry Pi (800x480)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Cargar fuentes
font = pygame.font.Font(r'fuentes/GamestationCond.otf', 50)
small_font = pygame.font.Font(r'fuentes/GamestationCond.otf', 24)
small_fontTabla = pygame.font.Font(r'fuentes/GamestationCond.otf', 50)

# Cargar imagen de fondo
fondo_menu = pygame.image.load(r'imagenes/Fondo_menu.png')
fondo_menu = pygame.transform.scale(fondo_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Cargar imagen de fondo para las preguntas
fondo_pregunta = pygame.image.load(r'imagenes/fondo_preguntas.png')
fondo_pregunta = pygame.transform.scale(fondo_pregunta, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Generar una pregunta de multiplicación aleatoria basada en la tabla seleccionada
def generar_pregunta(tabla_seleccionada):
    num1 = tabla_seleccionada
    num2 = random.randint(1, 12)
    resultado_correcto = num1 * num2
    respuestas = [resultado_correcto, random.randint(1, 144), random.randint(1, 144), random.randint(1, 144)]
    random.shuffle(respuestas)
    return num1, num2, resultado_correcto, respuestas

# Menú para seleccionar la tabla de multiplicar (2 al 12)
def menu_tabla_multiplicar(screen, volver_al_mapa):
    while True:
        screen.blit(fondo_menu, (0, 0))

        # Definir posiciones exactas de los botones en la imagen
        botones = {
            'Tabla del 2': pygame.Rect(110, 180, 170, 60),
            'Tabla del 3': pygame.Rect(110, 240, 170, 60),  # Subimos la fila de la Tabla del 3
            'Tabla del 4': pygame.Rect(110, 300, 170, 60),  # Subimos la fila de la Tabla del 4
            'Tabla del 5': pygame.Rect(110, 360, 170, 60),  # Subimos la fila de la Tabla del 5
            'Tabla del 6': pygame.Rect(320, 180, 170, 60),
            'Tabla del 7': pygame.Rect(320, 240, 170, 60),  # Subimos la fila de la Tabla del 7
            'Tabla del 8': pygame.Rect(320, 300, 170, 60),  # Subimos la fila de la Tabla del 8
            'Tabla del 9': pygame.Rect(320, 360, 170, 60),  # Subimos la fila de la Tabla del 9
            'Tabla del 10': pygame.Rect(530, 180, 170, 60),
            'Tabla del 11': pygame.Rect(530, 240, 170, 60),  # Subimos la fila de la Tabla del 11
            'Tabla del 12': pygame.Rect(530, 300, 170, 60)   # Subimos la fila de la Tabla del 12
        }

        # Dibujar botón "ATRÁS" en la esquina superior izquierda
        boton_atras = pygame.Rect(10, 10, 100, 40)
        pygame.draw.rect(screen, BLACK, boton_atras)
        mostrar_texto_centrado('ATRÁS', small_font, WHITE, boton_atras, screen)

        # Mostrar el texto en los botones, alineado y centrado
        for tabla, rect in botones.items():
            mostrar_texto_centrado(tabla, small_font, WHITE, rect, screen)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Detectar si se presiona el botón "ATRÁS"
                if boton_atras.collidepoint(mouse_pos):
                    return volver_al_mapa()  # Regresar al mapa de niveles

                # Detectar selección de tabla
                for tabla, rect in botones.items():
                    if rect.collidepoint(mouse_pos):
                        tabla_seleccionada = int(tabla.split()[-1])  # Extraer el número de la tabla seleccionada
                        return tabla_seleccionada  # Salimos del menú y pasamos a las preguntas

        pygame.display.update()

# Función de nivel con tabla seleccionada
def nivel(screen, volver_al_mapa, tabla_seleccionada):
    preguntas_restantes = 12
    aciertos = 0  # Contador de aciertos
    puntos = 0    # Contador de puntos (2 puntos por acierto)

    while preguntas_restantes > 0:
        # Mostrar el fondo de las preguntas
        screen.blit(fondo_pregunta, (0, 0))

        # Generar una pregunta aleatoria
        num1, num2, resultado_correcto, respuestas = generar_pregunta(tabla_seleccionada)

        # Mostrar la pregunta (centrada dentro del marco superior)
        mostrar_texto_centrado(f'{num1} x {num2} = ?', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 6 - 30, 300, 100), screen)

        # Mostrar las respuestas dentro de los botones rojos
        mostrar_texto_centrado(str(respuestas[0]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[1]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[2]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[3]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)

        # Dibujar los botones "Siguiente" y "Salir"
        dibujar_botones(screen)

        # Manejar eventos de selección de respuesta y botones
        respuesta_seleccionada = None
        resultado_mostrado = False
        while not resultado_mostrado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Detectar la respuesta seleccionada según la posición del clic
                    if SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 - 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 - 10:
                        respuesta_seleccionada = respuestas[0]
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 - 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 - 10:
                        respuesta_seleccionada = respuestas[1]
                    elif SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 + 40 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 90:
                        respuesta_seleccionada = respuestas[2]
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 + 40 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 90:
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
                    aciertos += 1  # Sumar un acierto
                    puntos += 2    # Sumar 2 puntos por acierto
                    mostrar_texto_centrado('¡Correcto!', font, GREEN, pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, 200, 50), screen)
                else:
                    mostrar_texto_centrado(f'¡Incorrecto! {num1} x {num2} = {resultado_correcto}', font, RED, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50), screen)
                                # Comprobar si la respuesta es correcta o incorrecta
            

            pygame.display.update()

        preguntas_restantes -= 1

    # Mostrar el puntaje final
    screen.fill(WHITE)
    mostrar_texto_centrado(f'Has terminado el nivel!', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)
    mostrar_texto_centrado(f'Aciertos: {aciertos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50), screen)
    mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50), screen)
    pygame.display.update()
    pygame.time.wait(5000)  # Esperar 3 segundos para mostrar el puntaje

    volver_al_mapa()

# Dibujar botones "Siguiente" y "Salir"
def dibujar_botones(screen):
    # Dibujar botón "Siguiente"
    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 180, SCREEN_HEIGHT - 80, 160, 50))
    mostrar_texto_centrado('Siguiente', small_font, WHITE, pygame.Rect(SCREEN_WIDTH - 180, SCREEN_HEIGHT - 80, 160, 50), screen)

    # Dibujar botón "Salir"
    pygame.draw.rect(screen, BLACK, (20, SCREEN_HEIGHT - 80, 160, 50))
    mostrar_texto_centrado('Salir', small_font, WHITE, pygame.Rect(20, SCREEN_HEIGHT - 80, 160, 50), screen)

# Nivel 1
def nivel_1(screen, volver_al_mapa):
    tabla_seleccionada = menu_tabla_multiplicar(screen, volver_al_mapa)
    if tabla_seleccionada:
        nivel(screen, volver_al_mapa, tabla_seleccionada)

# Nivel 2
def nivel_2(screen, volver_al_mapa):
    tabla_seleccionada = menu_tabla_multiplicar(screen, volver_al_mapa)
    if tabla_seleccionada:
        nivel(screen, volver_al_mapa, tabla_seleccionada)

# Nivel 3
def nivel_3(screen, volver_al_mapa):
    tabla_seleccionada = menu_tabla_multiplicar(screen, volver_al_mapa)
    if tabla_seleccionada:
        nivel(screen, volver_al_mapa, tabla_seleccionada)
