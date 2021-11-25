import pygame


class Fonts:

    # Not ideal as pygame needs to be initialized before calling Font or SysFont but this keeps errors from
    # occurring if you import the class
    def __init__(self):
        self.BASIC_FONT = pygame.font.Font('freesansbold.ttf', 40)
        self.MENU_FONT = pygame.font.SysFont('arial', 20)
        self.BIG_FONT = pygame.font.Font('freesansbold.ttf', 100)
