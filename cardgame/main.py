import pygame
from pygame.locals import *

import utils.utils
from cards.GeneralCard import GeneralCard
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
    my_card = GeneralCard(32, 0)
    my_other_card = GeneralCard(64, 64)
    card_list = [my_card, my_other_card]
    menu_surf, menu_rect = utils.utils.make_text_objs('MENU', fonts.MENU_FONT, colors.BLACK)
    game_state_manager = GameStateManager()
    menu_manager = MenuManager()

    while True:
        DISPLAYSURF.fill(colors.GRAY)

        menu_rect.topleft = (WINDOWWIDTH - 130, 0)
        DISPLAYSURF.blit(menu_surf, menu_rect)

        if game_state_manager.get_current_state() == GameStates.GAME:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_f:
                        pygame.display.toggle_fullscreen()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
                    for card in card_list:
                        if card.rect.collidepoint(pygame.mouse.get_pos()):
                            card.is_clicked = True
                            pygame.mouse.get_rel()
                    if menu_rect.collidepoint(pygame.mouse.get_pos()):
                        game_state_manager.set_game_state(GameStates.MENU)
                if event.type == MOUSEBUTTONUP:
                    for card in card_list:
                        if card.is_clicked is True:
                            card.is_clicked = False
                if event.type == pygame.MOUSEMOTION:
                    for card in card_list:
                        if card.is_clicked is True:
                            card.move_card(pygame.mouse.get_rel())
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
