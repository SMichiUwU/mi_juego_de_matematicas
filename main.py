import pygame
import sys
from niveles import nivel_1, nivel_2, nivel_3  # Importamos los niveles
from compartido import mostrar_texto_centrado  # Importamos la función compartida

# Inicializar Pygame
pygame.init()

# Configuración de pantalla para Raspberry Pi (800x480)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de Matemáticas - Mapa de Niveles')

# Cargar imagen de fondo del mapa
mapa_fondo = pygame.image.load(r'imagenes/mapa_juego.jpg')
mapa_fondo = pygame.transform.scale(mapa_fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Definir posiciones de los niveles en el mapa (x, y, radio del círculo ajustado)
niveles = {
    'Nivel 1': (150, 200, 40),  # Coordenadas (x, y) y radio del círculo más pequeño
    'Nivel 2': (400, 150, 40),
    'Nivel 3': (650, 300, 40)
}

# Cargar fuentes
font = pygame.font.Font(None, 60)  # Fuente más pequeña para adaptarse a la pantalla

# Función para mostrar el número dentro de un círculo
def mostrar_numero(numero, fuente, color, x, y):
    superficie = fuente.render(numero, True, color)
    rect = superficie.get_rect()
    rect.center = (x, y)
    screen.blit(superficie, rect)

# Función para el mapa de selección de niveles
def mapa_niveles():
    while True:
        screen.blit(mapa_fondo, (0, 0))  # Dibujar fondo del mapa

        # Dibujar los círculos de los niveles y los números en ellos
        for i, (nivel, (x, y, radio)) in enumerate(niveles.items(), start=1):
            pygame.draw.circle(screen, (255, 0, 0), (x, y), radio)  # Círculos rojos más pequeños
            mostrar_numero(str(i), font, (255, 255, 255), x, y)  # Números en blanco dentro de los círculos

        # Manejar eventos de selección de nivel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, (nivel, (x, y, radio)) in enumerate(niveles.items(), start=1):
                    if (x - radio) <= mouse_pos[0] <= (x + radio) and (y - radio) <= mouse_pos[1] <= (y + radio):
                        if i == 1:
                            nivel_1(screen, mapa_niveles)  # Inicia Nivel 1
                        elif i == 2:
                            nivel_2(screen, mapa_niveles)  # Inicia Nivel 2
                        elif i == 3:
                            nivel_3(screen, mapa_niveles)  # Inicia Nivel 3

        pygame.display.update()

# Ejecutar el mapa de niveles
mapa_niveles()