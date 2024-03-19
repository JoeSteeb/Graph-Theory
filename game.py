import pygame
import sys
from UI.menu import Menu
from UI.work_bench import Work_Bench
import UI.colour as colour
from IO.mouse import Mouse

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
mouse = Mouse()

# Button dimensions and positions
button_margin = 10
# Main loop
running = True
screen_width, screen_height = pygame.display.get_surface().get_size()
menu = Menu(screen, screen_width, screen_height)
work_bench = Work_Bench(screen)
while running:
    events = pygame.event.get()
    click = mouse.check_for_click(events)
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen_width, screen_height = pygame.display.get_surface().get_size()
    screen.fill(colour.white)
    menu.screen_width = screen_width
    menu.screen_height = screen_height    
    if not menu.draw(screen, click):
        work_bench.handle_click(click, menu.active_buttons, mouse)
        work_bench.handle_key_press(menu.active_buttons, events)
    work_bench.draw(menu.active_buttons)  
    
    pygame.display.flip()

pygame.quit()
sys.exit()
