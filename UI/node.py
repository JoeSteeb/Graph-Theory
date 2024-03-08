from .buttons import *
class Node:
    def __init__(self, text,location, n_id):
        self.text = text
        self.id = n_id
        self.degree = 0
        self.edges = []
        self.x = location[0]
        self.y = location[1]
        self.button = create_button("text", "circle", (location[0], location[1]))
        
    def add_edge(self,id):
        self.edges.append(id)
        self.degree+=1
        
    def draw(self, screen):
        self.button.draw(screen)