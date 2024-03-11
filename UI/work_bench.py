from .node import Node
from . import colour
from .edge import draw_edge

class Work_Bench:
    def __init__(self, screen):
        self.active_nodes = {}
        self.clicked_nodes = []
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
            
    def handle_click(self, click, menu_state):
        if not click:
            return
        print("Workbench detected click at: ", click)
        clicked_existing = False
        
        for node in self.active_nodes.values():
            if node.button.handle_click(click):
                node.button.shape.colour = colour.green
                self.clicked_nodes.append(node)
                if len(self.clicked_nodes) > 2:
                    self.clicked_nodes[0].button.shape.colour = colour.light_grey
                    self.clicked_nodes.pop(0)
                if len(self.clicked_nodes) > 1:
                    node.add_edge(self.clicked_nodes[0].id)
                clicked_existing = True
        if not clicked_existing:
            self.add_node(
                Node("TEST", click, self.current_id)
            )
        print("nodes = ", self.active_nodes)
        self.current_id+=1