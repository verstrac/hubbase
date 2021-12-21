import pygame

from utils import colors


class GeneralCard(pygame.sprite.Sprite):

    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.image.load('resources/BasicCard.png')

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
        self.is_clicked = False

    def move_card(self, x_and_y_rel):
        self.rect.x += x_and_y_rel[0]
        self.rect.y += x_and_y_rel[1]


