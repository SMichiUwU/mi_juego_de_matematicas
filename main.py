import pygame
import sys

# Inicializar Pygame
pygame.init()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de Matemáticas - Menú Principal')

# Cargar fuentes
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Función para mostrar texto en pantalla
def mostrar_texto(texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect()
    rect.center = (x, y)
    screen.blit(superficie, rect)

# Función del menú principal
def menu_principal():
    while True:
        screen.fill(WHITE)
        mostrar_texto('Juego de Matemáticas', font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        mostrar_texto('Presiona 1 para Nivel Básico', small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        mostrar_texto('Presiona 2 para Nivel Intermedio', small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        mostrar_texto('Presiona 3 para Nivel Avanzado', small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        mostrar_texto('Presiona Q para Salir', small_font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    seleccionar_nivel('Básico')
                elif event.key == pygame.K_2:
                    seleccionar_nivel('Intermedio')
                elif event.key == pygame.K_3:
                    seleccionar_nivel('Avanzado')
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Función para seleccionar nivel
def seleccionar_nivel(nivel):
    screen.fill(WHITE)
    mostrar_texto(f'Has seleccionado el nivel: {nivel}', font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.update()
    pygame.time.wait(2000)
    # Aquí podemos agregar la lógica para cargar las preguntas del nivel
    # Por ahora volvemos al menú principal
    menu_principal()

# Ejecutar el menú principal
menu_principal()
