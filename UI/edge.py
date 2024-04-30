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

    elif node1.id in node2.edges and node2.id in node1.edges:
        if abs(node1.y-node2.y) > node1.get_radius() * 2 + width:
            point1 = (node1.get_location()[0] + node1.get_radius() - width, node1.get_location()[1])
            point2 = (node2.get_location()[0] + node2.get_radius() - width, node2.get_location()[1])
            point3 = (node1.get_location()[0] - node1.get_radius() + width, node1.get_location()[1])
            point4 = (node2.get_location()[0] - node2.get_radius() + width, node2.get_location()[1])
            
            pygame.draw.line(screen, colour.red, point1, point2, 5)
            pygame.draw.line(screen, colour.red, point3, point4, 5)

        else:
            point1 = (node1.get_location()[0], node1.get_location()[1] + node1.get_radius() - width)
            point2 = (node2.get_location()[0], node2.get_location()[1] + node2.get_radius() - width)
            point3 = (node1.get_location()[0], node1.get_location()[1] - node1.get_radius() + width)
            point4 = (node2.get_location()[0], node2.get_location()[1] - node2.get_radius() + width)

            pygame.draw.line(screen, colour.red, point1, point2, 5)
            pygame.draw.line(screen, colour.red, point3, point4, 5)

        return [point1, point2, point3, point4]
    
    else:
        point1 = node1.get_location()
        point2 = node2.get_location()
        pygame.draw.line(screen, colour.red, node1.get_location(), node2.get_location(), 5)
        return([point1, point2])

def draw_directed_edge(screen, node1, node2):
    draw_edge(screen, node1, node2)
    