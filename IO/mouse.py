import pygame

class Mouse:
    def __init__(self):
        self.drag = False
        self.position = None
        
    def check_for_click(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.drag = True
                return pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                self.drag = False
                return pygame.mouse.get_pos()
            self.position = pygame.mouse.get_pos()
        return None
