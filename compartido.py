import pygame
import sys

# Función compartida para mostrar texto centrado
def mostrar_texto_centrado(texto, fuente, color, rect, screen):
    superficie = fuente.render(texto, True, color)
    texto_rect = superficie.get_rect()
    texto_rect.center = (rect.x + rect.width // 2, rect.y + rect.height // 2 + 5)  # Centrado con ajuste
    screen.blit(superficie, texto_rect)
