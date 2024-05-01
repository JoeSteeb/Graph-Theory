import pygame
import math
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
    points = draw_edge(screen, node1, node2)
    if points and len(points) < 3:
        x1 = points[0][0]
        x2 = points[1][0]
        y1 = points[0][1]
        y2 = points[1][1]
        
        opposite = y2 - y1
        hypotenuse = math.sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))
        
        angle = math.asin(opposite/hypotenuse) 
        perpendicular_angle = angle + math.pi / 2
        
        half = hypotenuse / 2
        normal_x = math.cos(angle)
        normal_y = math.sin(angle)
        
        perpendicular_normal_x = math.cos(perpendicular_angle)
        perpendicular_normal_y = math.sin(perpendicular_angle)
        
        if(x1 > x2):
            perpendicular_normal_x *= -1
            normal_x *= -1
            
                        
        mid_x_1 = normal_x * half + x1
        mid_y_1 = normal_y * half + y1
        
        mid_x_2 = normal_x * (half + 20) + x1
        mid_y_2 = normal_y * (half + 20) + y1
        
        croshair_x_1 = perpendicular_normal_x * 10 + mid_x_1
        croshair_y_1 = perpendicular_normal_y * 10 + mid_y_1
        croshair_x_2 = perpendicular_normal_x * -10 + mid_x_1
        croshair_y_2 = perpendicular_normal_y * -10 + mid_y_1
        
        pygame.draw.polygon(screen, colour.black, 
                         [(croshair_x_1, croshair_y_1),
                          (croshair_x_2, croshair_y_2),
                          (mid_x_2, mid_y_2)])
        
    