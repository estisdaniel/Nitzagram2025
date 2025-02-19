import pygame
from constants import *
from Post import Post
from helpers import screen

class imagepost(Post):
    def __init__(self,image_path,user_name,loction,discription):
        super().__init__(user_name,loction,discription)
        self.image= pygame.image.load(image_path)
        img = pygame.image.load(image_path)
        img = pygame.transform.scale(img,POST_WIDTH,POST_HEIGHT)

    def display_discription(self,):

        font = pygame.font.SysFont('chalkduster' , (UI_FONT_SIZE))
        text = font.render((self.discription),True ,(0, 0, 0))
        screen.blit(text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        pass
    def display_likes(self):

        font = pygame.font.SysFont('chalkduster' , (UI_FONT_SIZE))
        text = font.render((f"liked by {self.likes_counters} users"), True, (0, 0, 0))
        screen.blit(text, (LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS))

        pass
    def display_name(self):
        font = pygame.font.SysFont('chalkduster', (UI_FONT_SIZE))
        text = font.render(self.user_name, True, (0, 0, 0))
        screen.blit(text, (USER_NAME_X_POS, USER_NAME_Y_POS))

        pass
    def display_comments(self):

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

    def display_text_location(self):

        font = pygame.font.SysFont('chalkduster' , (UI_FONT_SIZE))
        text = font.render(self.loction, True, (0, 0, 0))
        screen.blit(text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        pass

    def display_content(self,img):
        screen.blit(img,(POST_X_POS,POST_Y_POS))