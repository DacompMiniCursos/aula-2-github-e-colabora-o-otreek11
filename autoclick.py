import mouse                    # pip install mouse
import keyboard                 # pip install keyboard
from pygame.time import Clock   # pip install pygame

# Configs
CPS: int = 180                  # clicks per second
QUIT_KEY: str = 'q'             # macro quit key
ONOFF_KEY: str = 'k'            # macro on/off key
CLICKER: str = 'm'              # 'k' for keyboard, 'm' for mouse
CLICKED_KEY: str = 'left'       # key to be clicked

# Internal Variables
clock = Clock()
running = True
should_click = False
onoff_pressed = False
func = keyboard.press if CLICKER == 'k' else mouse.click

# Main code
if __name__ == "__main__":
    while running:
        if should_click:
            func(CLICKED_KEY)
        if keyboard.is_pressed(QUIT_KEY):
            running = False
        if keyboard.is_pressed(ONOFF_KEY):
            if not onoff_pressed:
                should_click = not should_click
            onoff_pressed = True
        else:
            onoff_pressed = False
                
        clock.tick(CPS)