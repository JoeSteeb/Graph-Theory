import pygame
import sys
import UI.menu as menu
import UI.colour as colour
import IO.mouse as mouse

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

# Button dimensions and positions
button_margin = 10
# Main loop
running = True
while running:
    click = mouse.check_for_click()
    screen_width, screen_height = pygame.display.get_surface().get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(colour.white)
    
    # Draw Menu
    menu.draw_menu(screen, screen_height, click)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
