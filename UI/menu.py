import pygame
from . import colour
from .buttons import *

button_width, button_height = 200, 40
button_margin = 10

class Menu:
    
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.active_buttons = {}
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.active_buttons["place_node"] = create_button("Place Node", "rectangle", (10, screen_height-100))
        self.active_buttons["place_edge"] = create_button("Place Edge", "rectangle", (10, screen_height-50))
        
        
    def draw(self, screen, click):
        clicked = False
        for button in self.active_buttons.values():
            if click:
                if button.handle_click(click):
                    clicked = True
            # print(button.text,"clicked?: ", button.clicked)
            if button.clicked:
                button.shape.colour = colour.green
                print("menu button clicked")
            else:
                button.shape.colour = colour.light_grey                
            button.draw(screen)
        return clicked

        
