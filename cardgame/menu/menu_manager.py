import pygame

import utils.utils
from menu.game_menu import GameMenu


class MenuManager:
    def __init__(self):
        self.game_menu = None
        self.displayed = False

    def set_displayed(self, is_displayed):
        self.displayed = is_displayed

    def is_displayed(self):
        return self.displayed

    def initialize_menu(self, window_height, window_width, containers):
        GameMenu.containers = containers
        self.game_menu = GameMenu(window_height, window_width)
        self.displayed = True

    def remove_menu(self):
        self.game_menu.kill()
        self.game_menu = None
        self.displayed = False

    def handle_event(self, events):
        for event in events.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_menu.is_close_button_clicked(event.pos):
                    self.remove_menu()
                elif self.game_menu.is_quit_button_clicked(event.pos):
                    utils.utils.terminate()
