import pygame
import sys
from UI.menu import Menu
from UI.work_bench import Work_Bench
import UI.colour as colour
import IO.mouse as mouse

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

# Button dimensions and positions
button_margin = 10
# Main loop
running = True
screen_width, screen_height = pygame.display.get_surface().get_size()
menu = Menu(screen, screen_width, screen_height)
work_bench = Work_Bench(screen)
while running:
    click = mouse.check_for_click()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen_width, screen_height = pygame.display.get_surface().get_size()
    screen.fill(colour.white)
    menu.screen_width = screen_width
    menu.screen_height = screen_height
    # Draw Menu
    if not menu.draw(screen, click):
        work_bench.handle_click(click, work_bench.active_nodes)  
    work_bench.draw()  
    pygame.display.flip()

pygame.quit()
sys.exit()
