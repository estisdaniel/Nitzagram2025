import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, user_name, loction, discription):
        self.user_name = user_name
        self.loction = loction
        self.likes_counters = []
        self.comments = []
        self.discription = discription

        pass

    def display(self):

        font = pygame.font.SysFont('chalkduster' , (UI_FONT_SIZE))
        text = font.render('eitan romanov', True, (0, 0, 0))
        screen.blit(text, (USER_NAME_X_POS, USER_NAME_Y_POS))


        text = font.render('Ashdod', True, (0, 0, 0))
        screen.blit(text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        text = font.render((f"liked by {self.likes_counters} users"), True, (0, 0, 0))
        screen.blit(text, (LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS))


        pass


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



