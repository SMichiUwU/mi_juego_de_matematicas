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
    
    # Generar tres respuestas incorrectas que no sean iguales al resultado correcto
    respuestas_incorrectas = set()
    while len(respuestas_incorrectas) < 3:
        respuesta = random.randint(1, 144)
        if respuesta != resultado_correcto:
            respuestas_incorrectas.add(respuesta)

    respuestas = [resultado_correcto] + list(respuestas_incorrectas)
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

# Función para mostrar un mensaje con fondo (Correcto o Incorrecto)
def mostrar_mensaje_con_fondo(screen, mensaje, fuente, color_texto, color_fondo, rect):
    # Dibujar el fondo (rectángulo)
    pygame.draw.rect(screen, color_fondo, rect)
    # Mostrar el mensaje centrado en el rectángulo
    mostrar_texto_centrado(mensaje, fuente, color_texto, rect, screen)

# Función de nivel con tabla seleccionada
def nivel(screen, volver_al_mapa, tabla_seleccionada):
    preguntas_restantes = 12
    aciertos = 0  # Contador de aciertos
    puntos = 0    # Contador de puntos (2 puntos por acierto)
    vidas = 5     # Vidas totales del juego (5 oportunidades en total)

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

        # Mostrar los puntos en la esquina superior derecha
        mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 40), screen)

        # Mostrar las vidas totales en la esquina superior izquierda
        mostrar_texto_centrado(f'Vidas: {vidas}', small_font, BLACK, pygame.Rect(10, 10, 190, 40), screen)

        # Dibujar los botones "Siguiente" y "Salir"
        dibujar_botones(screen)

        respuesta_seleccionada = None
        resultado_mostrado = False

        while not resultado_mostrado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Limpiar la pantalla para quitar mensajes anteriores
                    screen.blit(fondo_pregunta, (0, 0))
                    mostrar_texto_centrado(f'{num1} x {num2} = ?', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 6 - 30, 300, 100), screen)

                    # Volver a mostrar las respuestas y botones
                    mostrar_texto_centrado(str(respuestas[0]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
                    mostrar_texto_centrado(str(respuestas[1]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
                    mostrar_texto_centrado(str(respuestas[2]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)
                    mostrar_texto_centrado(str(respuestas[3]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)
                    
                    # Volver a mostrar los puntos y las vidas totales
                    mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 40), screen)
                    mostrar_texto_centrado(f'Vidas: {vidas}', small_font, BLACK, pygame.Rect(10, 10, 190, 40), screen)

                    # Volver a dibujar botones
                    dibujar_botones(screen)

                    # Detectar la respuesta seleccionada según la posición del clic
                    if SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 - 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 - 10:
                        respuesta_seleccionada = respuestas[0]
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 - 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 - 10:
                        respuesta_seleccionada = respuestas[1]
                    elif SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 + 40 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 90:
                        respuesta_seleccionada = respuestas[2]
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 + 40 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 90:
                        respuesta_seleccionada = respuestas[3]

                    if respuesta_seleccionada is not None:
                        # Comprobar si la respuesta es correcta o incorrecta
                        if respuesta_seleccionada == resultado_correcto:
                            aciertos += 1  # Sumar un acierto
                            puntos += 2    # Sumar 2 puntos por acierto
                            mostrar_mensaje_con_fondo(screen, '¡Correcto!', font, WHITE, GREEN, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()

                            # Esperar 3 segundos y pasar a la siguiente pregunta automáticamente
                            pygame.time.wait(1000)
                            resultado_mostrado = True  # Salir del bucle para ir a la siguiente pregunta
                        else:
                            vidas -= 1  # Quitar una vida por intento fallido
                            mostrar_mensaje_con_fondo(screen, '¡Incorrecto! Inténtalo de nuevo.', small_font, WHITE, RED, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()

                            # Esperar 1 segundo para mostrar el mensaje de incorrecto y luego limpiarlo
                            pygame.time.wait(1000)

                            # Limpiar la pantalla nuevamente (solo si la respuesta es incorrecta)
                            screen.blit(fondo_pregunta, (0, 0))
                            mostrar_texto_centrado(f'{num1} x {num2} = ?', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 6 - 30, 300, 100), screen)

                            # Volver a mostrar las respuestas, puntos y vidas
                            mostrar_texto_centrado(str(respuestas[0]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
                            mostrar_texto_centrado(str(respuestas[1]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
                            mostrar_texto_centrado(str(respuestas[2]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)
                            mostrar_texto_centrado(str(respuestas[3]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)
                            mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 40), screen)
                            mostrar_texto_centrado(f'Vidas: {vidas}', small_font, BLACK, pygame.Rect(10, 10, 190, 40), screen)

                            dibujar_botones(screen)

                            # Si el jugador pierde todas las vidas, finalizar el juego
                            if vidas == 0:
                                game_over(screen, puntos, volver_al_mapa)
                                return  # Finalizar el juego

                    # Comprobar si se hace clic en el botón "Siguiente" (solo disponible en caso de error)
                    if SCREEN_WIDTH - 180 <= mouse_pos[0] <= SCREEN_WIDTH - 20 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        resultado_mostrado = True  # Salir del bucle cuando se presiona "Siguiente"

                    # Comprobar si se hace clic en el botón "Salir"
                    if 20 <= mouse_pos[0] <= 180 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        return  # Regresar al menú de selección de tablas

            pygame.display.update()

        preguntas_restantes -= 1

    # Mostrar el puntaje final
    screen.fill(WHITE)
    mostrar_texto_centrado(f'Has terminado el nivel!', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)
    mostrar_texto_centrado(f'Aciertos: {aciertos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50), screen)
    mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50), screen)
    pygame.display.update()
    pygame.time.wait(5000)  # Esperar 5 segundos para mostrar el puntaje

    volver_al_mapa()

# Función para mostrar pantalla de "Game Over" cuando el jugador pierde
def game_over(screen, puntos, volver_al_mapa):
    screen.fill(WHITE)
    mostrar_texto_centrado('¡Has perdido!', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)
    mostrar_texto_centrado(f'Total Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50), screen)
    mostrar_texto_centrado('Inténtalo de nuevo', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50), screen)
    pygame.display.update()
    
    # Esperar 5 segundos antes de volver al mapa de tablas
    pygame.time.wait(5000)
    volver_al_mapa()  # Redirigir al menú de selección de tablas

# Generar una pregunta aleatoria para el segundo nivel con respuestas correctas
def generar_pregunta_segundo_nivel():
    tipo_pregunta = random.choice(["multiplicacion_dos_digitos", "combinacion_operaciones", "resultado_faltante"])
    
    if tipo_pregunta == "multiplicacion_dos_digitos":
        # Multiplicación con dos dígitos
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        resultado_correcto = num1 * num2
        
        # Generar respuestas incorrectas distintas y únicas
        respuestas_incorrectas = set()
        while len(respuestas_incorrectas) < 3:
            incorrecta = random.randint(100, 9999)
            if incorrecta != resultado_correcto:
                respuestas_incorrectas.add(incorrecta)
        
        # Añadir la respuesta correcta y mezclar
        respuestas = [resultado_correcto] + list(respuestas_incorrectas)
        random.shuffle(respuestas)
        pregunta = f"{num1} x {num2} = ?"
        return pregunta, resultado_correcto, respuestas

    elif tipo_pregunta == "combinacion_operaciones":
        # Combinación de operaciones: multiplicación + suma o resta
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        num3 = random.randint(1, 10)
        operacion = random.choice(["+", "-"])
        
        if operacion == "+":
            resultado_correcto = num1 * num2 + num3
            pregunta = f"{num1} x {num2} + {num3} = ?"
        else:
            resultado_correcto = num1 * num2 - num3
            pregunta = f"{num1} x {num2} - {num3} = ?"
        
        respuestas_incorrectas = set()
        while len(respuestas_incorrectas) < 3:
            incorrecta = random.randint(10, 100)
            if incorrecta != resultado_correcto:
                respuestas_incorrectas.add(incorrecta)
        
        respuestas = [resultado_correcto] + list(respuestas_incorrectas)
        random.shuffle(respuestas)
        return pregunta, resultado_correcto, respuestas

    elif tipo_pregunta == "resultado_faltante":
        # Multiplicación con número faltante
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        resultado_correcto = num1 * num2
        posicion_faltante = random.choice([1, 2])  # Falta el primer número o el segundo

        if posicion_faltante == 1:
            pregunta = f"? x {num2} = {resultado_correcto}"
            respuestas = [num1, random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)]
        else:
            pregunta = f"{num1} x ? = {resultado_correcto}"
            respuestas = [num2, random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)]

        random.shuffle(respuestas)
        return pregunta, num1 if posicion_faltante == 1 else num2, respuestas

# Función del segundo nivel
def nivel_2(screen, volver_al_mapa):
    preguntas_restantes = 12
    aciertos = 0  # Contador de aciertos
    puntos = 0    # Contador de puntos (2 puntos por acierto)
    vidas = 7     # Vidas totales del juego (7 oportunidades en total)

    while preguntas_restantes > 0 and vidas > 0:
        # Generar una pregunta aleatoria del segundo nivel
        pregunta, resultado_correcto, respuestas = generar_pregunta_segundo_nivel()

        # Mostrar el fondo de las preguntas
        screen.blit(fondo_pregunta, (0, 0))

        # Mostrar la pregunta centrada
        mostrar_texto_centrado(pregunta, font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 6 - 30, 300, 100), screen)

        # Mostrar las respuestas dentro de los botones
        mostrar_texto_centrado(str(respuestas[0]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[1]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[2]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)
        mostrar_texto_centrado(str(respuestas[3]), small_fontTabla, BLACK, pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50), screen)

        # Mostrar los puntos y las vidas
        mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 40), screen)
        mostrar_texto_centrado(f'Vidas: {vidas}', small_font, BLACK, pygame.Rect(10, 10, 190, 40), screen)

        # Dibujar los botones "Siguiente" y "Salir"
        dibujar_botones(screen)

        respuesta_seleccionada = None
        ha_respondido = False  # Verifica si el jugador ya seleccionó una respuesta
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
                        ha_respondido = True
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 - 60 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 - 10:
                        respuesta_seleccionada = respuestas[1]
                        ha_respondido = True
                    elif SCREEN_WIDTH // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH // 3 + 50 and SCREEN_HEIGHT // 2 + 40 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 90:
                        respuesta_seleccionada = respuestas[2]
                        ha_respondido = True
                    elif SCREEN_WIDTH * 2 // 3 - 50 <= mouse_pos[0] <= SCREEN_WIDTH * 2 // 3 + 50 and SCREEN_HEIGHT // 2 + 40 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 90:
                        respuesta_seleccionada = respuestas[3]
                        ha_respondido = True

                    if respuesta_seleccionada is not None:
                        # Comprobar si la respuesta es correcta o incorrecta
                        if respuesta_seleccionada == resultado_correcto:
                            aciertos += 1  # Sumar un acierto
                            puntos += 2    # Sumar 2 puntos por acierto
                            mostrar_mensaje_con_fondo(screen, '¡Correcto!', font, WHITE, GREEN, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()
                            pygame.time.wait(500)  # Mostrar el mensaje "¡Correcto!" por 0.5 segundos
                            resultado_mostrado = True
                        else:
                            vidas -= 1  # Quitar una vida por intento fallido
                            mostrar_mensaje_con_fondo(screen, '¡Incorrecto! Inténtalo de nuevo.', small_font, WHITE, RED, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()
                            pygame.time.wait(500)  # Mostrar el mensaje "¡Incorrecto!" por 0.5 segundos
                            resultado_mostrado = False  # Permitir al jugador intentar de nuevo sin avanzar
                            # Aquí hacemos que el mensaje desaparezca y continúe
                            continue  # Volver al bucle para que pueda seleccionar otra respuesta

                    # Comprobar si se hace clic en el botón "Siguiente" para avanzar
                    if SCREEN_WIDTH - 180 <= mouse_pos[0] <= SCREEN_WIDTH - 20 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        if not ha_respondido:
                            vidas -= 1  # Restar una vida si el jugador no respondió antes de pasar
                            mostrar_mensaje_con_fondo(screen, '¡Incorrecto! No respondiste.', small_font, WHITE, RED, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()
                            pygame.time.wait(500)  # Mostrar el mensaje por 0.5 segundos
                        resultado_mostrado = True

                    # Comprobar si se hace clic en el botón "Salir"
                    if 20 <= mouse_pos[0] <= 180 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        return volver_al_mapa()  # Regresar al mapa de niveles sin penalización

            pygame.display.update()

        preguntas_restantes -= 1

    # Mostrar el puntaje final
    screen.fill(WHITE)
    mostrar_texto_centrado(f'Has terminado el nivel!', font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)
    mostrar_texto_centrado(f'Aciertos: {aciertos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50), screen)
    mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50), screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Mostrar el puntaje por 3 segundos antes de volver al mapa

    volver_al_mapa()

# Función para mostrar un mensaje con fondo (Correcto o Incorrecto)
def mostrar_mensaje_con_fondo(screen, mensaje, fuente, color_texto, color_fondo, rect):
    pygame.draw.rect(screen, color_fondo, rect)
    mostrar_texto_centrado(mensaje, fuente, color_texto, rect, screen)

# Dibujar botones "Siguiente" y "Salir"
def dibujar_botones(screen):
    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 180, SCREEN_HEIGHT - 80, 160, 50))
    mostrar_texto_centrado('Siguiente', small_font, WHITE, pygame.Rect(SCREEN_WIDTH - 180, SCREEN_HEIGHT - 80, 160, 50), screen)

    pygame.draw.rect(screen, BLACK, (20, SCREEN_HEIGHT - 80, 160, 50))
    mostrar_texto_centrado('Salir', small_font, WHITE, pygame.Rect(20, SCREEN_HEIGHT - 80, 160, 50), screen)

# Nivel 1
def nivel_1(screen, volver_al_mapa):
    tabla_seleccionada = menu_tabla_multiplicar(screen, volver_al_mapa)
    if tabla_seleccionada:
        nivel(screen, volver_al_mapa, tabla_seleccionada)



def nivel_3(screen, volver_al_mapa):
  return