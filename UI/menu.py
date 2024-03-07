import pygame
from . import colour
from .buttons import *

button_width, button_height = 200, 40
button_margin = 10

# Button texts
buttons = [("Create Node", lambda x: print("Create Node")), ("Create Edge", lambda x: print("Create Edge"))]
 
def draw_button(screen, x, y, width=200, height=40, text="NONE"):
    pygame.draw.rect(screen, colour.grey, [x, y, width, height])
    
def draw_menu(screen, screen_height, click):
    button = create_button("Click Me Click Me Click Me", "circle", (100, 200),onclick=lambda: print("clicked"))
    if click:
        button.handle_click(click)
    button.draw(screen)

        
