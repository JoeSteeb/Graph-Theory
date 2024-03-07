import pygame
from . import colour

class Shape:
    def __init__(self, x, y, color=colour.light_grey):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        pass  # To be implemented by subclasses

class Circle(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_click(self, position):
        # Calculate distance from circle center to click position
        distance = ((position[0] - self.x) ** 2 + (position[1] - self.y) ** 2) ** 0.5
        return distance <= self.radius

class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def check_click(self, position):
        return (self.x <= position[0] <= self.x + self.width) and (self.y <= position[1] <= self.y + self.height)

class Button:
    def __init__(self, shape, x, y, onclick, text='', font_size=30, text_color=colour.black):
        self.shape = shape
        self.x = x
        self.y = y
        self.onclick = onclick
        self.text = text
        self.font_size = font_size
        self.text_color = text_color

    def draw(self, screen):
        self.shape.draw(screen)
        font = pygame.font.Font(None, self.font_size)
        text_render = font.render(self.text, True, self.text_color)
        screen.blit(text_render, (self.x, self.y))

    def handle_click(self, position):
        if(self.shape.check_click(position)):
            self.onclick()
            return True
        else:
            return False
        
def create_button(text, shape_type, position, text_color='black', background_color='light_grey', onclick=lambda: None):
    # Determine text size
    font_size = 30
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, getattr(colour, text_color))
    text_width, text_height = text_render.get_size()

    # Add padding
    padding = 10
    text_width += padding * 2
    text_height += padding * 2

    # Use provided position
    x, y = position  # Now position is directly used

    # Instantiate the correct shape based on the shape type
    if shape_type.lower() == 'rectangle':
        shape = Rectangle(x, y, text_width, text_height, getattr(colour, background_color))
    elif shape_type.lower() == 'circle':
        # For a circle, we'll consider the text_width as the diameter for simplicity
        # Adjust circle's x and y to be at the center of the text
        radius = max(text_width, text_height) // 2
        shape = Circle(x + radius - padding, y + radius - padding, radius, getattr(colour, background_color))
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

    # Create and return the button with the new shape and provided text, font size, and colors
    return Button(shape, x, y, onclick, text=text, font_size=font_size, text_color=getattr(colour, text_color))