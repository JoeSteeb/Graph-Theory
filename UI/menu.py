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
        self.collapsed = False

        # List of button names and their respective titles
        buttons_info = [
            ("edit_lable", "Edit Lable"),  # Maintaining original spelling
            ("place_node", "Place Vertex"),
            ("delete_node", "Remove Vertex"),
            ("place_edge", "Place Edge"),
            ("show_degree", "Show Degree")
        ]

        # Calculate the starting y position dynamically based on the number of buttons
        total_buttons_height = len(buttons_info) * button_height + (len(buttons_info) - 1) * button_margin
        start_y = screen_height - total_buttons_height
        
        # Creating buttons and setting their positions dynamically
        for i, (key, title) in enumerate(buttons_info):
            button_y = start_y + i * (button_height + button_margin)
            self.active_buttons[key] = create_button(title, "rectangle", (10, button_y))

        
        
    def draw(self, screen, click):
        clicked = False
        for button in self.active_buttons.values():
            if click:
                if button.handle_click(click):
                    clicked = True
            # print(button.text,"clicked?: ", button.clicked)
            if button.clicked:
                for button2 in self.active_buttons.values():
                    if button2 != button:
                        button2.clicked = False
                        button2.shape.colour = colour.light_grey
                button.shape.colour = colour.green
                # print("menu button clicked")
            else:
                button.shape.colour = colour.light_grey                
            button.draw(screen)
        return clicked

        
