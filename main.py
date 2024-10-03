import pygame
import sys
from menu_niveles import mapa_niveles


# Inicializar Pygame
pygame.init()

# Configuración de pantalla para Raspberry Pi (800x480)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Menú Principal - Juego Educativo')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Cargar imagen de fondo (opcional, si tienes una imagen para el fondo del menú principal)
fondo_menu = pygame.image.load(r'imagenes/fondo_menu.jpg')
fondo_menu = pygame.transform.scale(fondo_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Definir fuentes
font = pygame.font.Font(None, 50)

# Función para mostrar texto centrado en un botón
def mostrar_texto_centrado(superficie, texto, x, y, ancho, alto, color):
    label = font.render(texto, True, color)
    rect = label.get_rect(center=(x + ancho // 2, y + alto // 2))
    superficie.blit(label, rect)

# Función para mostrar el menú principal
def menu_principal():
    while True:
        # Dibujar el fondo del menú
        screen.blit(fondo_menu, (0, 0))

        # Definir botones del menú principal
        boton_juego = pygame.Rect(250, 120, 300, 70)
        boton_opcion2 = pygame.Rect(250, 220, 300, 70)
        boton_acerca = pygame.Rect(250, 320, 300, 70)

        # Dibujar los botones
        pygame.draw.rect(screen, RED, boton_juego)
        
        pygame.draw.rect(screen, BLUE, boton_opcion2)
        pygame.draw.rect(screen, (0, 200, 0), boton_acerca)

        # Mostrar texto en cada botón
        mostrar_texto_centrado(screen, 'Juego de Niveles', boton_juego.x, boton_juego.y, boton_juego.width, boton_juego.height, WHITE)
        mostrar_texto_centrado(screen, 'Interaccion', boton_opcion2.x, boton_opcion2.y, boton_opcion2.width, boton_opcion2.height, WHITE)
        mostrar_texto_centrado(screen, 'Acerca de', boton_acerca.x, boton_acerca.y, boton_acerca.width, boton_acerca.height, WHITE)

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_juego.collidepoint(event.pos):
                    mapa_niveles()  # Llamar a la función `mapa_niveles` cuando se presione el botón Juego de Niveles
                elif boton_opcion2.collidepoint(event.pos):
                    print("Segunda Opción seleccionada (por definir).")
                elif boton_acerca.collidepoint(event.pos):
                    mostrar_acerca()  # Llamar a la función `mostrar_acerca` cuando se presione el botón Acerca de

        pygame.display.update()

# Función para mostrar información acerca del proyecto
def mostrar_acerca():
    while True:
        screen.fill(BLACK)
        mostrar_texto_centrado(screen, 'Juego creado por el equipo de Desarrollo.', 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE)
        mostrar_texto_centrado(screen, 'Presiona cualquier tecla para regresar.', 0, 100, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                menu_principal()  # Regresar al menú principal

        pygame.display.update()

# Ejecutar el menú principal
menu_principal()
