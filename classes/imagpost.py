import pygame
from constants import *
from Post import Post
from helpers import screen


class imagepost(Post):
    def __init__(self,image_path,user_name,loction,discription):
        super().__init__(user_name,loction,discription)
        self.image= pygame.image.load(image_path)
        img= pygame.image.load(image_path)
        img= pygame.transform.scale(img,POST_WIDTH,POST_HEIGHT)

    def display_discription(self,):

    def display_likes(self):

    def display_name(self):

    def display_comments(self):

    def display_text_location(self):
