import pygame
def check_for_click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Return the mouse position (x, y) at the time of the click
            return pygame.mouse.get_pos()
    # Return None if no click was detected
    return None
