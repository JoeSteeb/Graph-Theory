import pygame

class Keyboard:
    def __init__(self):
        pass
    
    @staticmethod
    def check_for_key_press(events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                print("key pressed: ", event)
                return event
        return None
    
    @staticmethod
    def modify_str(string, key):
        # Check if the key is backspace
        if key.key == 8:
            print("BACKSPACE")
            return string[:-1]
        elif key.unicode.isprintable():
            return string + key.unicode
        else:
            return string
