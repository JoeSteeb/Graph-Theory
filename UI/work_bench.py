from .node import Node
from . import colour
from .edge import draw_edge

class Work_Bench:
    def __init__(self, screen):
        self.active_nodes = {}
        self.clicked_nodes = []
        self.current_click = None
        self.screen = screen
        self.current_id = 0
        
    def add_node(self, node):
        self.active_nodes[node.id] = node
    
    def draw(self):
        # if len(self.clicked_nodes) > 1:
        #     draw_edge(self.screen, self.clicked_nodes[0], self.clicked_nodes[1])
        for node in self.active_nodes.values():
            for id in node.edges:
                draw_edge(self.screen, self.active_nodes[id], node)       
        for node in self.active_nodes.values():    
            node.draw(self.screen)
            
    def handle_click(self, click, menu_buttons, mouse):
            
        if mouse.drag:
            if self.current_click:
                self.current_click.handle_movement(mouse.position)
        else:
            self.current_click = None
        if not click:
            return
        print("Workbench detected click at: ", click)
        clicked_existing = False
        
        for node in self.active_nodes.values():
            if node.handle_click(click):
                self.current_click = node
                if menu_buttons["place_edge"].clicked:
                    node.button.shape.colour = colour.green
                    self.clicked_nodes.append(node)
                    if len(self.clicked_nodes) > 2:
                        for n in self.clicked_nodes:
                            n.button.shape.colour = colour.light_grey
                        self.clicked_nodes = []
                    if len(self.clicked_nodes) > 1:
                        node.add_edge(self.clicked_nodes[0].id)
                clicked_existing = True
        if not clicked_existing:
            self.add_node(
                Node("TEST", click, self.current_id)
            )
        print("nodes = ", self.active_nodes)
        self.current_id+=1