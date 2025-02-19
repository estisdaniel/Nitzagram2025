import pygame
from Post import Post


class text_post:
    def __init__(self, text, text_color, background_color):
        self.text = text
        self.text_color = text_color
        self.background = background_color

    def display(self):
        font = pygame.font.SysFont('chalkduster', (40))
        text = font.render(self.text, True, self.text_color)
        screen.blit()





