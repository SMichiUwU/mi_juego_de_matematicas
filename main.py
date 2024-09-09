import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de Matemáticas - Mapa de Niveles')

# Cargar imagen de fondo del mapa
mapa_fondo = pygame.image.load(r'C:\Users\USER\Documents\UTEQ\TRABAJS\amorcito\tesis\mi_juego_de_matematicas\imagenes\mapa_juego.jpg')  # Coloca aquí tu imagen de mapa
mapa_fondo = pygame.transform.scale(mapa_fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Definir posiciones de los niveles en el mapa
niveles = {
    'Nivel Básico': (200, 300),
    'Nivel Intermedio': (400, 200),
    'Nivel Avanzado': (600, 400)
}

# Cargar fuentes
font = pygame.font.Font(None, 36)

# Función para mostrar texto
def mostrar_texto(texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = (x, y)
    screen.blit(superficie, rect)

# Función para el mapa de selección de niveles
def mapa_niveles():
    while True:
        screen.blit(mapa_fondo, (0, 0))  # Dibujar fondo del mapa

        # Dibujar los niveles en el mapa
        for nivel, pos in niveles.items():
            pygame.draw.circle(screen, (255, 0, 0), pos, 20)  # Círculos rojos que representan los niveles
            mostrar_texto(nivel, font, (0, 0, 0), pos[0], pos[1] - 30)  # Mostrar nombres de los niveles

        # Manejar eventos de selección de nivel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for nivel, pos in niveles.items():
                    if (pos[0] - 20) <= mouse_pos[0] <= (pos[0] + 20) and (pos[1] - 20) <= mouse_pos[1] <= (pos[1] + 20):
                        seleccionar_nivel(nivel)

        pygame.display.update()

# Función para seleccionar nivel
def seleccionar_nivel(nivel):
    screen.fill((255, 255, 255))
    mostrar_texto(f'Has seleccionado el {nivel}', font, (0, 255, 0), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.update()
    pygame.time.wait(2000)
    # Aquí podríamos agregar la lógica para comenzar el nivel específico (tablas de multiplicar, etc.)
    mapa_niveles()

# Ejecutar el mapa de niveles
mapa_niveles()
