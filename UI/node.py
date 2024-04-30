from .buttons import *
class Node:
    def __init__(self, text,location, n_id):
        self.text = text
        self.lable = text
        self.id = n_id
        self.degree = 0
        self.edges = []
        self.display_mode = "text"
        self.x = location[0]
        self.y = location[1]
        self.last_position = None
        self.button = create_button("", "circle", (location[0], location[1]))
    
    def get_location(self):
        return (self.button.x, self.button.y)
    
    def handle_click(self, position):
        clicked = self.button.handle_click(position)
        if clicked:
            self.last_position = position
        else:
            self.last_position = None
        return clicked
    
    def move(self, position):
        self.x = position[0]
        self.y = position[1]
        self.button.move(position[0], position[1])
        
    def handle_movement(self, click):
        if self.last_position and click != self.last_position:
            self.move(click)
            
    def get_radius(self):
        return self.button.shape.get_radius()
            
        # print("movement")
    
    def add_edge(self, id):
        self.edges.append(id)
        self.degree+=1
        
    def remove_edge(self, id):
        if id in self.edges:
            self.edges.remove(id)
        
    def draw(self, screen):
        self.button.draw(screen)