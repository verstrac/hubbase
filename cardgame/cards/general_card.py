import pygame

from utils import colors, utils
from utils.fonts import Fonts

CARD_WIDTH = 80

class GeneralCard(pygame.sprite.Sprite):

    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        fonts = Fonts()
        self.card_number = 10
        self.image = pygame.image.load('resources/BasicCard.png')

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
        self.is_clicked = False

        # Create number on on right lower corner of card.
        menu_font = fonts.MENU_FONT
        self.close_surf, self.close_rect = utils.make_text_objs(str(self.card_number), menu_font, colors.BLACK)
        self.close_rect.x = CARD_WIDTH - 20
        self.close_rect.y = 100
        self.image.blit(self.close_surf, self.close_rect)

    def move_card(self, x_and_y_rel):
        self.rect.x += x_and_y_rel[0]
        self.rect.y += x_and_y_rel[1]


