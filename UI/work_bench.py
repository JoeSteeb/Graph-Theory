from .node import Node
from . import colour
from .edge import draw_edge
from IO.keyboard import Keyboard
import pygame

class Work_Bench:
    def __init__(self, screen):
        self.active_nodes = {}
        self.clicked_nodes = []
        self.current_click = None
        self.screen = screen
        self.current_id = 0
        self.keyboard = Keyboard()
        
    def add_node(self, node):
        self.active_nodes[node.id] = node
    
    def draw(self, active_buttons):
        # if len(self.clicked_nodes) > 1:
        #     draw_edge(self.screen, self.clicked_nodes[0], self.clicked_nodes[1])
        for node in self.active_nodes.values():
            for id in node.edges:
                draw_edge(self.screen, self.active_nodes[id], node)       
        for node in self.active_nodes.values():    
            node.draw(self.screen)
            if not active_buttons["place_edge"].clicked and  not active_buttons["edit_lable"].clicked:
                node.button.shape.colour = colour.light_grey
                self.clicked_nodes = []
    
    def handle_key_press(self, menu_buttons, events):
        key = self.keyboard.check_for_key_press(events)
        if not menu_buttons["edit_lable"] or not key:
            return
        if key == pygame.K_BACKSPACE:
            print("BACKSPACE")
        for node in self.clicked_nodes:
            node.button.text = self.keyboard.modify_str(node.button.text, key)
        
                        
    def handle_click(self, click, menu_buttons, mouse):
            
        if mouse.drag:
            if self.current_click:
                self.current_click.handle_movement(mouse.position)
        else:
            self.current_click = None
        if not click:
            return
        print("menu state: ", menu_buttons)
        print("Workbench detected click at: ", click)
        clicked_existing = False
        
        for node in self.active_nodes.values():
            if node.handle_click(click):
                self.current_click = node
                clicked_existing = True
        if self.current_click:
            if menu_buttons["place_edge"].clicked:
                self.current_click.button.shape.colour = colour.green
                self.clicked_nodes.append(self.current_click)
                if len(self.clicked_nodes) > 1:
                    self.current_click.add_edge(self.clicked_nodes[0].id)
                    for n in self.clicked_nodes:
                        n.button.shape.colour = colour.light_grey
                    self.clicked_nodes = []
                    
            elif menu_buttons["delete_node"].clicked:
                # remove dependent adjacencies
                for node in self.active_nodes.values():
                    node.remove_edge(self.current_click.id)
                self.active_nodes.pop(self.current_click.id)
                
            elif menu_buttons["edit_lable"].clicked:
                if self.current_click:
                    self.clicked_nodes += [self.current_click]
                    self.current_click.button.shape.colour = colour.light_green
                                
                    
        if not clicked_existing:
            self.add_node(
                Node("TEST", click, self.current_id)
            )
        # print("nodes = ", self.active_nodes)
        self.current_id+=1