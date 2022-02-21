import pygame

from utils import colors, utils
from utils.fonts import Fonts

CARD_WIDTH = 80

class GeneralCard(pygame.sprite.Sprite):

    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.fonts = Fonts()
        self.card_number = 10
        self.image = pygame.image.load('resources/BasicCard.png')

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
        self.is_clicked = False

        # Create number on right lower corner of card.
        self.lower_right_image = pygame.image.load('resources/Number1.png')
        self.lower_right_rect = self.lower_right_image.get_rect()
        self.lower_right_rect.x = CARD_WIDTH - 28
        self.lower_right_rect.y = 90
        self.image.blit(self.lower_right_image, self.lower_right_rect)

        # Create number on left lower corner of card
        self.lower_left_image = pygame.image.load('resources/NumberSheet.png').subsurface(32, 0, 32, 32)
        self.lower_left_rect = self.lower_left_image.get_rect()
        self.lower_left_rect.x = 5
        self.lower_left_rect.y = 90
        self.image.blit(self.lower_left_image, self.lower_left_rect)

    def move_card(self, x_and_y_rel):
        self.rect.x += x_and_y_rel[0]
        self.rect.y += x_and_y_rel[1]

    def change_card_number(self, new_number):
        self.image = pygame.image.load('resources/BasicCard.png')
        self.number_surface, self.number_rect = utils.make_text_objs(str(new_number), self.fonts.MENU_FONT, colors.BLACK)
        self.number_rect.x = CARD_WIDTH - 20
        self.number_rect.y = 100
        self.image.blit(self.number_surface, self.number_rect)
