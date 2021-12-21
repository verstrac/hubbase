import pygame
from pygame.locals import *

import utils.utils
from cards.general_card import GeneralCard
from cards.card_manager import CardManager
from cards.stronghold_card import StrongholdCard
from menu.menu_manager import MenuManager
from state.game_state_manager import GameStateManager
from utils import colors
from utils.fonts import Fonts
from utils.game_states import GameStates

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
FPS = 60


def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE)
    FPSCLOCK = pygame.time.Clock()
    while True:
        run_game()


def run_game():
    fonts = Fonts()
    render_update_group = pygame.sprite.RenderUpdates()
    GeneralCard.containers = render_update_group
    StrongholdCard.containers = render_update_group
    card_manager = CardManager()
    menu_surf, menu_rect = utils.utils.make_text_objs('MENU', fonts.MENU_FONT, colors.BLACK)
    game_state_manager = GameStateManager()
    menu_manager = MenuManager()
    stronghold = pygame.image.load('resources/Stronghold.png')
    stronghold.get_rect().topleft = (0, 0)

    while True:
        DISPLAYSURF.fill(colors.GRAY)

        menu_rect.topleft = (WINDOWWIDTH - 130, 0)
        DISPLAYSURF.blit(menu_surf, menu_rect)

        if game_state_manager.get_current_state() == GameStates.GAME:
            card_manager.card_event(pygame.event, menu_rect, game_state_manager)
        elif game_state_manager.get_current_state() == GameStates.MENU:
            if menu_manager.game_menu is None:
                menu_manager.initialize_menu(WINDOWHEIGHT, WINDOWWIDTH, render_update_group)
            menu_manager.handle_event(pygame.event)
            if not menu_manager.is_displayed():
                game_state_manager.set_game_state(GameStates.GAME)

        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, DISPLAYSURF)

        # update all the sprites
        render_update_group.update()

        dirty = render_update_group.draw(DISPLAYSURF)

        pygame.display.update(dirty)

        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
