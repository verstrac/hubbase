import pygame

from utils import colors, utils
from utils.fonts import Fonts

MENU_WIDTH = 300
MENU_HEIGHT = 200


class GameMenu(pygame.sprite.Sprite):
    def __init__(self, window_height, window_width):
        pygame.sprite.Sprite.__init__(self, self.containers)
        fonts = Fonts()
        # init the containing window height and width so that we can use them later to calculate the relative
        # position of mouse clicks
        self.containing_window_height = window_height
        self.containing_window_width = window_width

        # set the is display initialize to false
        self.is_displayed = False

        # create the menu surface and rectangle
        self.image = pygame.Surface((MENU_WIDTH, MENU_HEIGHT))
        self.rect = pygame.Rect(window_width / 2 - 150, window_height / 2 - 100, MENU_WIDTH, MENU_HEIGHT)

        # fill in the surface with a background color
        self.image.fill(colors.BLACK)

        # draw the menu boarder
        pygame.draw.rect(self.image, (212, 175, 155),
                         (0, 0, MENU_WIDTH, MENU_HEIGHT), 5)

        # create the quit text and add it to the menu
        menu_font = fonts.MENU_FONT
        self.quit_surf, self.quit_rect = utils.make_text_objs("Quit", menu_font, colors.RED)
        self.quit_rect.midtop = (MENU_WIDTH / 2, 10)
        self.image.blit(self.quit_surf, self.quit_rect)

        # create the close menu 'X'
        self.close_surf, self.close_rect = utils.make_text_objs("X", menu_font, colors.RED)
        self.close_rect.x = MENU_WIDTH - 38
        self.close_rect.y = 5
        self.image.blit(self.close_surf, self.close_rect)

        # create the fullscreen text and add it to the menu
        menu_font = fonts.MENU_FONT
        self.fullscreen_surf, self.fullscreen_rect = utils.make_text_objs("Fullscreen", menu_font, colors.RED)
        self.fullscreen_rect.midtop = (MENU_WIDTH / 2, 35)
        self.image.blit(self.fullscreen_surf, self.fullscreen_rect)

    def is_quit_button_clicked(self, pos):
        gap_between_menu_and_window_horizontal = self.containing_window_width / 2 - MENU_WIDTH / 2
        x_pos = pos[0] - gap_between_menu_and_window_horizontal
        gap_between_menu_and_window_vertical = self.containing_window_height / 2 - MENU_HEIGHT / 2
        y_pos = pos[1] - gap_between_menu_and_window_vertical
        return self.quit_rect.collidepoint(x_pos, y_pos)

    def is_close_button_clicked(self, pos):
        gap_between_menu_and_window_horizontal = self.containing_window_width / 2 - MENU_WIDTH / 2
        x_pos = pos[0] - gap_between_menu_and_window_horizontal
        gap_between_menu_and_window_vertical = self.containing_window_height / 2 - MENU_HEIGHT / 2
        y_pos = pos[1] - gap_between_menu_and_window_vertical
        return self.close_rect.collidepoint(x_pos, y_pos)

    def is_fullscreen_button_clicked(self, pos):
        gap_between_menu_and_window_horizontal = self.containing_window_width / 2 - MENU_WIDTH / 2
        x_pos = pos[0] - gap_between_menu_and_window_horizontal
        gap_between_menu_and_window_vertical = self.containing_window_height / 2 - MENU_HEIGHT / 2
        y_pos = pos[1] - gap_between_menu_and_window_vertical
        return self.fullscreen_rect.collidepoint(x_pos, y_pos)