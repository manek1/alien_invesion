import pygame
# blit() to draw the image.
# load() to load image
# get_rect() - get dimensions of any image as rectangle


class Ship:
    """This will create ship for our game"""
    def __init__(self, screen):
        """Initialize ship & its starting position"""
        self.screen = screen

        # Load the ship image & get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitem(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

