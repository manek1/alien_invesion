import sys
import pygame
import settings
from ship import Ship


# 1. We need screen(display) with game name where player will play game
# 2. We need games name


def run_game():
    """initialize game & create screen object"""
    # Initialize background settings for pygame
    pygame.init()
    ai_settings = settings.Settings()

    # Create display surface
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption(ai_settings.caption)

    # Create ship
    sunny_ship = Ship(screen)

    # set background color
    bg_color = ai_settings.bg_color  # RBG range from 0-255(255, 0, 0) - Red, (0, 255, 0) - Blue, (0, 0, 255) - Green

    # Start main loop for the game
    # Watch for Keyboard & mouse event

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        sunny_ship.blitem()
        # make the most recent screen drawn visible
        pygame.display.flip()


run_game()
