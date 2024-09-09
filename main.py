import pygame
import sys
from niveles import nivel_1, nivel_2, nivel_3  # Importamos los niveles

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de Matemáticas - Mapa de Niveles')

# Cargar imagen de fondo del mapa
mapa_fondo = pygame.image.load(r'imagenes/mapa_juego.jpg')
mapa_fondo = pygame.transform.scale(mapa_fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Definir posiciones de los niveles en el mapa
niveles = {
    'Nivel 1': (200, 300, 50),
    'Nivel 2': (400, 200, 50),
    'Nivel 3': (600, 400, 50)
}

# Cargar fuentes
font = pygame.font.Font(None, 74)

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
            pygame.draw.circle(screen, (255, 0, 0), (x, y), radio)  # Círculos rojos
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
                            nivel_1()  # Inicia Nivel 1
                        elif i == 2:
                            nivel_2()  # Inicia Nivel 2
                        elif i == 3:
                            nivel_3()  # Inicia Nivel 3

        pygame.display.update()

# Ejecutar el mapa de niveles
mapa_niveles()
