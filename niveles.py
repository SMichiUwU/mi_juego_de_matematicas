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
 #def nivel_2(screen, volver_al_mapa):
  
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

def nivel_2(screen, volver_al_mapa):
    preguntas_restantes = 12
    aciertos = 0  # Contador de aciertos
    puntos = 0    # Contador de puntos (2 puntos por acierto)
    vidas = 7     # Vidas totales del juego (7 oportunidades en total)
    mensaje_mostrado = False  # Para manejar el tiempo de visualización de mensajes

    # Colores para los mensajes
    COLOR_CORRECTO = (0, 255, 0)
    COLOR_INCORRECTO = (255, 0, 0)

    while preguntas_restantes > 0 and vidas > 0:
        # Generar una pregunta aleatoria del segundo nivel
        pregunta, resultado_correcto, respuestas = generar_pregunta_segundo_nivel()

        # Rectángulos para la presentación de respuestas
        rect_pregunta = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 6 - 30, 300, 100)
        rect_respuestas = [
            pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50),
            pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 - 60, 100, 50),
            pygame.Rect(SCREEN_WIDTH // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50),
            pygame.Rect(SCREEN_WIDTH * 2 // 3 - 50, SCREEN_HEIGHT // 2 + 40, 100, 50)
        ]

        # Mostrar la pregunta inicial y las respuestas
        screen.blit(fondo_pregunta, (0, 0))  # Fondo inicial
        mostrar_texto_centrado(pregunta, font, BLACK, rect_pregunta, screen)
        for idx, rect in enumerate(rect_respuestas):
            mostrar_texto_centrado(str(respuestas[idx]), small_fontTabla, BLACK, rect, screen)
        mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 40), screen)
        mostrar_texto_centrado(f'Vidas: {vidas}', small_font, BLACK, pygame.Rect(10, 10, 190, 40), screen)
        dibujar_botones(screen)
        pygame.display.update()  # Actualizar la pantalla inicial

        respuesta_seleccionada = None
        resultado_mostrado = False
        ha_respondido = False  # Para evitar penalizar antes de seleccionar una respuesta
        tiempo_inicio_mensaje = None
        mostrar_correcto = False  # Bandera para mostrar el mensaje "¡Correcto!"

        while not resultado_mostrado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Detectar la respuesta seleccionada
                    for idx, rect in enumerate(rect_respuestas):
                        if rect.collidepoint(mouse_pos):
                            respuesta_seleccionada = respuestas[idx]
                            ha_respondido = True

                    # Detectar botón "Siguiente"
                    if SCREEN_WIDTH - 180 <= mouse_pos[0] <= SCREEN_WIDTH - 20 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        if not ha_respondido:
                            vidas -= 1  # Penalizar por no responder antes de pasar
                            mensaje_mostrado = True
                            tiempo_inicio_mensaje = pygame.time.get_ticks()
                            mostrar_mensaje_con_fondo(screen, '¡Incorrecto! No respondiste.', small_font, WHITE, COLOR_INCORRECTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()
                        resultado_mostrado = True

                    # Detectar botón "Salir"
                    if 20 <= mouse_pos[0] <= 180 and SCREEN_HEIGHT - 80 <= mouse_pos[1] <= SCREEN_HEIGHT - 30:
                        return volver_al_mapa()  # Regresar al mapa de niveles

                    # Verificar si la respuesta seleccionada es correcta
                    if respuesta_seleccionada is not None:
                        if respuesta_seleccionada == resultado_correcto:
                            aciertos += 1
                            puntos += 2
                            mensaje_mostrado = True
                            mostrar_correcto = True  # Bandera para mostrar "¡Correcto!"
                            tiempo_inicio_mensaje = pygame.time.get_ticks()
                            # Mostrar mensaje "¡Correcto!" en color verde y centrarlo
                            mostrar_mensaje_con_fondo(screen, '¡Correcto!', font, WHITE, COLOR_CORRECTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()
                            resultado_mostrado = True  # Salir del bucle para la siguiente pregunta
                        else:
                            vidas -= 1
                            mensaje_mostrado = True
                            mostrar_correcto = False  # Bandera para no mostrar "¡Correcto!"
                            tiempo_inicio_mensaje = pygame.time.get_ticks()
                            # Mostrar mensaje "¡Incorrecto!" en color rojo
                            mostrar_mensaje_con_fondo(screen, '¡Incorrecto! Inténtalo de nuevo.', small_font, WHITE, COLOR_INCORRECTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 150, 300, 50))
                            pygame.display.update()
                            respuesta_seleccionada = None  # Permitir reintento
                            ha_respondido = False

            # Mostrar mensajes por un breve período sin bloquear el flujo
            if mensaje_mostrado and tiempo_inicio_mensaje:
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - tiempo_inicio_mensaje >= 1000:  # Mostrar por 1 segundo
                    mensaje_mostrado = False
                    tiempo_inicio_mensaje = None
                    # Limpiar mensaje y mostrar pregunta nuevamente
                    screen.blit(fondo_pregunta, (0, 0))
                    mostrar_texto_centrado(pregunta, font, BLACK, rect_pregunta, screen)
                    for idx, rect in enumerate(rect_respuestas):
                        mostrar_texto_centrado(str(respuestas[idx]), small_fontTabla, BLACK, rect, screen)
                    mostrar_texto_centrado(f'Puntos: {puntos}', small_font, BLACK, pygame.Rect(SCREEN_WIDTH - 200, 10, 190, 40), screen)
                    mostrar_texto_centrado(f'Vidas: {vidas}', small_font, BLACK, pygame.Rect(10, 10, 190, 40), screen)
                    dibujar_botones(screen)
                    pygame.display.update()  # Refrescar la pantalla con la nueva pregunta y opciones

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



#-------------- nivel tres 

import pygame
import random
import sys

# Definir colores y configuración
COLOR_JUGADOR = (0, 255, 0)  # Verde para la barra de vida del jugador
COLOR_ENEMIGO = (255, 0, 0)  # Rojo para la barra de vida del enemigo
COLOR_FONDO = (200, 200, 200)  # Fondo de pantalla para contraste
COLOR_TEXTO = (0, 0, 0)  # Negro para el texto
COLOR_BOTONES = (255, 255, 255)  # Blanco para los botones de respuesta

# Variables de vida
VIDA_JUGADOR = 100
VIDA_ENEMIGO = 100

# Configuración de tamaño de pantalla y fuentes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
pygame.init()
font = pygame.font.Font(None, 30)  # Tamaño de fuente ajustado para el enunciado
small_font = pygame.font.Font(None, 28)  # Fuente ajustada para las respuestas

# Cargar imágenes del jugador y del enemigo
imagen_jugador = pygame.image.load(r'imagenes/jugador.png')
imagen_jugador = pygame.transform.scale(imagen_jugador, (100, 100))
imagen_enemigo = pygame.image.load(r'imagenes/enemigo.png')
imagen_enemigo = pygame.transform.scale(imagen_enemigo, (100, 100))

# Cargar imágenes de los proyectiles (espada y lanza)
imagen_espada = pygame.image.load(r'imagenes/espada.png')  # Imagen de la espada del jugador
imagen_espada = pygame.transform.scale(imagen_espada, (50, 10))  # Redimensionar para proyectil

imagen_lanza = pygame.image.load(r'imagenes/lanza.png')  # Imagen de la lanza del enemigo
imagen_lanza = pygame.transform.scale(imagen_lanza, (50, 10))  # Redimensionar para proyectil

# Generar preguntas de razonamiento basadas en multiplicación para la batalla
def generar_pregunta_razonamiento_multiplicacion():
    preguntas = [
        ("Si tengo 4 cajas y cada caja tiene 5 manzanas, ¿cuántas manzanas hay en total?", 20, [10, 15, 20, 25]),
        ("¿Cuántas ruedas hay en 7 coches si cada coche tiene 4 ruedas?", 28, [24, 28, 32, 30]),
        ("Si hay 3 grupos de 8 niños, ¿cuántos niños hay en total?", 24, [16, 20, 24, 32]),
        ("Un edificio tiene 5 pisos y cada piso tiene 6 ventanas, ¿cuántas ventanas hay?", 30, [20, 25, 30, 35]),
        ("En un cine hay 9 filas con 12 asientos cada una, ¿cuántos asientos hay en total?", 108, [100, 108, 120, 112]),
        ("Si compras 6 paquetes con 7 caramelos cada uno, ¿cuántos caramelos tienes?", 42, [36, 42, 45, 49]),
        ("Hay 8 cajas y cada caja contiene 9 libros, ¿cuántos libros hay en total?", 72, [72, 64, 81, 88])
    ]
    pregunta, respuesta_correcta, opciones = random.choice(preguntas)
    return pregunta, respuesta_correcta, opciones

# Dibujar la barra de vida del jugador y del enemigo
def dibujar_barra_vida(screen, vida_jugador, vida_enemigo):
    # Barra de vida del jugador
    pygame.draw.rect(screen, COLOR_JUGADOR, (50, 50, vida_jugador * 2, 30))  # Escalar la vida a 200 píxeles
    mostrar_texto_centrado(f'Jugador: {vida_jugador}%', small_font, COLOR_TEXTO, pygame.Rect(50, 20, 200, 30), screen)

    # Barra de vida del enemigo
    pygame.draw.rect(screen, COLOR_ENEMIGO, (550, 50, vida_enemigo * 2, 30))  # Escalar la vida a 200 píxeles
    mostrar_texto_centrado(f'Enemigo: {vida_enemigo}%', small_font, COLOR_TEXTO, pygame.Rect(550, 20, 200, 30), screen)

# Animación del ataque del jugador y el enemigo
def animar_ataque(screen, proyectil, inicio_x, inicio_y, final_x, final_y, velocidad=10):
    x, y = inicio_x, inicio_y
    while (x < final_x and inicio_x < final_x) or (x > final_x and inicio_x > final_x):
        screen.blit(proyectil, (x, y))  # Dibujar el proyectil en la posición actual
        pygame.display.update()
        pygame.time.delay(50)  # Pausa para animación
        screen.fill(COLOR_FONDO, (x, y, proyectil.get_width(), proyectil.get_height()))  # Limpiar la posición anterior
        x += velocidad if inicio_x < final_x else -velocidad  # Mover en la dirección correcta

# Función para dividir y centrar el enunciado en dos líneas
def mostrar_texto_doble_linea(texto, fuente, color, rect, screen):
    palabras = texto.split()
    linea1 = " ".join(palabras[:len(palabras) // 2])
    linea2 = " ".join(palabras[len(palabras) // 2:])
    
    # Mostrar la primera línea en la mitad superior del rectángulo
    texto_surface1 = fuente.render(linea1, True, color)
    texto_rect1 = texto_surface1.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 4))
    screen.blit(texto_surface1, texto_rect1)
    
    # Mostrar la segunda línea en la mitad inferior del rectángulo
    texto_surface2 = fuente.render(linea2, True, color)
    texto_rect2 = texto_surface2.get_rect(center=(rect.x + rect.width // 2, rect.y + 3 * rect.height // 4))
    screen.blit(texto_surface2, texto_rect2)

# Función de nivel 3 - Batalla Matemática
def nivel_3(screen, volver_al_mapa):
    vida_jugador = VIDA_JUGADOR
    vida_enemigo = VIDA_ENEMIGO
    ronda_actual = 1
    max_rondas = 5

    # Fondo de pantalla para la batalla
    fondo_pregunta = pygame.image.load(r'imagenes/nivel3.png')
    fondo_pregunta = pygame.transform.scale(fondo_pregunta, (SCREEN_WIDTH, SCREEN_HEIGHT))

    while vida_jugador > 0 and vida_enemigo > 0 and ronda_actual <= max_rondas:
        # Mostrar fondo
        screen.blit(fondo_pregunta, (0, 0))

        # Dibujar barra de vida del jugador y del enemigo
        dibujar_barra_vida(screen, vida_jugador, vida_enemigo)

        # Mostrar imágenes del jugador y del enemigo en la parte inferior
        screen.blit(imagen_jugador, (50, SCREEN_HEIGHT - 150))  # Jugador en la parte inferior izquierda
        screen.blit(imagen_enemigo, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 150))  # Enemigo en la parte inferior derecha

        # Generar pregunta y mostrarla
        pregunta, respuesta_correcta, respuestas = generar_pregunta_razonamiento_multiplicacion()
        # Mostrar la pregunta en dos líneas, posicionada más abajo para dejar espacio para la barra de vida
        mostrar_texto_doble_linea(pregunta, font, COLOR_TEXTO, pygame.Rect(SCREEN_WIDTH // 2 - 300, 120, 600, 100), screen)

        # Dibujar respuestas en una sola fila, más arriba en la pantalla (altura de 250)
        rect_respuestas = [
            pygame.Rect(100 + i * 150, 250, 100, 50)  # Posiciones alineadas más arriba en la pantalla
            for i in range(4)
        ]

        for idx, rect in enumerate(rect_respuestas):
            pygame.draw.rect(screen, COLOR_BOTONES, rect)  # Dibujar el fondo del botón
            mostrar_texto_centrado(str(respuestas[idx]), small_font, COLOR_TEXTO, rect, screen)

        pygame.display.update()  # Actualizar pantalla con las respuestas

        # Bucle de eventos para seleccionar una respuesta
        respuesta_seleccionada = None
        while respuesta_seleccionada is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for idx, rect in enumerate(rect_respuestas):
                        if rect.collidepoint(mouse_pos):
                            respuesta_seleccionada = respuestas[idx]

            pygame.display.update()

        # Verificar si la respuesta es correcta
        if respuesta_seleccionada == respuesta_correcta:
            # El jugador ataca al enemigo con la espada
            animar_ataque(screen, imagen_espada, 150, SCREEN_HEIGHT - 100, SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100)
            vida_enemigo -= 20
            mostrar_texto_centrado('¡Correcto! Atacaste al enemigo.', small_font, COLOR_TEXTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50), screen)
        else:
            # El enemigo ataca al jugador con la lanza hacia la izquierda
            animar_ataque(screen, imagen_lanza, SCREEN_WIDTH - 150, SCREEN_HEIGHT - 100, 150, SCREEN_HEIGHT - 100)
            vida_jugador -= 20
            mostrar_texto_centrado('¡Incorrecto! El enemigo te atacó.', small_font, COLOR_TEXTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50), screen)

        pygame.display.update()
        pygame.time.wait(1000)  # Pausa para mostrar el mensaje

        ronda_actual += 1  # Incrementar la ronda

    # Final de la batalla
    screen.fill(COLOR_FONDO)
    if vida_enemigo <= 0:
        mostrar_texto_centrado('¡Ganaste la batalla!', font, COLOR_TEXTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)
    elif vida_jugador <= 0:
        mostrar_texto_centrado('¡Perdiste la batalla!', font, COLOR_TEXTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)
    else:
        mostrar_texto_centrado('¡Batalla terminada!', font, COLOR_TEXTO, pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50), screen)

    pygame.display.update()
    pygame.time.wait(3000)  # Pausa antes de volver al mapa

    volver_al_mapa()  # Volver al mapa de niveles

# Mostrar texto centrado en un rectángulo
def mostrar_texto_centrado(texto, fuente, color, rect, screen):
    superficie = fuente.render(texto, True, color)
    texto_rect = superficie.get_rect()
    texto_rect.center = (rect.x + rect.width // 2, rect.y + rect.height // 2)
    screen.blit(superficie, texto_rect)

