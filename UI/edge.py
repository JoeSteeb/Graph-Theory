import pygame
from . import colour

def draw_edge(screen, node1, node2):
    width = 5
    if node1 == node2:  # Check if node1 is the same as node2
        x, y = node1.get_location()
        # Define points for the triangle
        point1 = (x+node1.get_radius()-width, y)
        point2 = (x-node1.get_radius()+width, y)
        point3 = (x, y - node1.get_radius() * 2)
        # Draw the triangle
        pygame.draw.line(screen, colour.red, point1, point3, width)
        pygame.draw.line(screen, colour.red, point2, point3, width)
    else:
        pygame.draw.line(screen, colour.red, node1.get_location(), node2.get_location(), 5)
