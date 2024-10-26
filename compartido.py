import os
import pygame

# Inicializar el módulo de fuentes de Pygame
pygame.font.init()

# Determina el directorio base del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Función para obtener la ruta completa de un recurso
def obtener_ruta_recurso(ruta_relativa):
    return os.path.join(BASE_DIR, ruta_relativa)

# Función compartida para mostrar texto centrado
def mostrar_texto_centrado(texto, fuente, color, rect, screen):
    superficie = fuente.render(texto, True, color)
    texto_rect = superficie.get_rect()
    texto_rect.center = (rect.x + rect.width // 2, rect.y + rect.height // 2 + 5)  # Centrado con ajuste
    screen.blit(superficie, texto_rect)

# Función para cargar una fuente con tamaño específico
def cargar_fuente(tamaño):
    ruta_fuente = obtener_ruta_recurso('fuentes/Comicsans.otf')  # Ruta a la fuente que usas
    return pygame.font.Font(ruta_fuente, tamaño)

# Cargar las fuentes con los tamaños que necesitas
font_principal = cargar_fuente(40)  # Fuente principal tamaño 40
small_font = cargar_fuente(20)  # Fuente para botones tamaño 20
small_font_tabla = cargar_fuente(40)  # Otra fuente con tamaño 40 (puede ser para títulos de tablas)
smaller_font = cargar_fuente(18)  # Fuente más pequeña tamaño 18
font_mediana = cargar_fuente(30)  # Fuente mediana tamaño 30
font_medium = cargar_fuente(25)  # Fuente mediana tamaño 25