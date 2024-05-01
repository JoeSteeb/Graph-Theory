from .node import Node
from . import colour
from .edge import draw_edge, draw_directed_edge
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
        self.font= pygame.font.Font(None, 20)
        
    def add_node(self, node):
        self.active_nodes[node.id] = node
    
    def draw(self, active_buttons):
        for node in self.active_nodes.values():
            for id in node.edges:
                if(active_buttons["directed"].clicked):
                    draw_directed_edge(self.screen, self.active_nodes[id], node)       
                else:
                    draw_edge(self.screen, self.active_nodes[id], node)
        edge_count = 0
        for node in self.active_nodes.values(): 
            if(active_buttons["show_degree"].clicked):
                node.button.text = str(node.degree)
            else:
                node.button.text = node.text
                
            node.draw(self.screen)
            if not active_buttons["place_edge"].clicked and  not active_buttons["edit_lable"].clicked:
                node.button.shape.colour = colour.light_grey
                self.clicked_nodes = []
            edge_count += len(node.edges)
                
        vertex_text = self.font.render("Vertex Count: " + str(len(self.active_nodes)), True, colour.black)
        edge_text = self.font.render("Edge Count: " + str(edge_count), True, colour.black)        
        vertex_text_rect = vertex_text.get_rect()
        edge_text_rect = edge_text.get_rect()
        vertex_text_rect.topleft = (10, 10)  # Center the text
        edge_text_rect.topleft = (10, 25)
        self.screen.blit(vertex_text, vertex_text_rect)
        self.screen.blit(edge_text, edge_text_rect)
    
    def handle_key_press(self, menu_buttons, events):
        key = self.keyboard.check_for_key_press(events)
        if not menu_buttons["edit_lable"] or not key:
            return
        if key == pygame.K_BACKSPACE:
            print("BACKSPACE")
        for node in self.clicked_nodes:
            node.text = self.keyboard.modify_str(node.text, key)
        
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
        clicked_existing = self.process_click_on_existing_nodes(click)
        self.process_menu_actions(menu_buttons, clicked_existing, click)
    
    def process_click_on_existing_nodes(self, click):
        clicked_existing = False
        for node in self.active_nodes.values():
            if node.handle_click(click):
                self.current_click = node
                clicked_existing = True
        return clicked_existing
    
    def process_menu_actions(self, menu_buttons, clicked_existing, click):
        if self.current_click:
            if menu_buttons["place_edge"].clicked:
                self.handle_place_edge()
            elif menu_buttons["delete_node"].clicked:
                self.handle_delete_node()
            elif menu_buttons["edit_lable"].clicked:
                self.handle_edit_label()
                    
        if not clicked_existing:
            if not menu_buttons["place_node"].clicked:
                self.clicked_nodes = []
                return
            self.add_node(
                Node("", click, self.current_id)
            )
            self.current_id += 1

    def handle_place_edge(self):
        self.current_click.button.shape.colour = colour.green
        self.clicked_nodes.append(self.current_click)
        if len(self.clicked_nodes) > 1:
            self.current_click.add_edge(self.clicked_nodes[0])
            for n in self.clicked_nodes:
                n.button.shape.colour = colour.light_grey
            self.clicked_nodes = []

    def handle_delete_node(self):
        for id in self.current_click.edges:
            self.active_nodes[id].degree -= 1
        for node in self.active_nodes.values():
            node.remove_edge(self.current_click.id)
        self.active_nodes.pop(self.current_click.id)
        

    def handle_edit_label(self):
        for n in self.clicked_nodes:
                n.button.shape.colour = colour.light_grey
        self.clicked_nodes = [self.current_click]
        self.current_click.button.shape.colour = colour.light_green
