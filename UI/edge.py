import pygame
from . import colour

def draw_edge(screen, node1, node2):
    pygame.draw.line(screen, colour.red, (node1.x, node1.y), (node2.x, node2.y), 5)
