from .node import Node

class Work_Bench:
    def __init__(self, screen):
        self.active_nodes = {}
        self.screen = screen
        self.current_id = 0
        
    def add_node(self, node):
        self.active_nodes[node.id] = node
    
    def draw(self):
        for node in self.active_nodes.values():
            node.draw(self.screen)
            
    def handle_click(self, click, menu_state):
        if not click:
            return
        print("Workbench detected click at: ", click)
        self.add_node(
            Node("TEST", click, self.current_id)
        )
        self.current_id+=1