import pygame

from utils import Colors


class GeneralCard(pygame.sprite.Sprite):

    def __init__(self, x_position, y_position):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.Surface((32, 32))
        pygame.draw.rect(self.image, Colors.RED, (0, 0, 32, 32))

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position