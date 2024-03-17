import pygame
from . import colour

def draw_edge(screen, node1, node2):
    pygame.draw.line(screen, colour.red, (node1.get_location()), (node2.get_location()), 5)
