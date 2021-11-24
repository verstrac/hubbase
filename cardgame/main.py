import sys
import pygame
from pygame.locals import *

import utils.Utils
from cards.GeneralCard import GeneralCard
from utils import Colors
from utils.Fonts import Fonts

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
    menu_surf, menu_rect = utils.Utils.make_text_objs('MENU', fonts.MENU_FONT, Colors.BLACK)



    while True:
        checkForQuit()

        DISPLAYSURF.fill(Colors.GRAY)

        menu_rect.topleft = (WINDOWWIDTH - 130, 0)
        DISPLAYSURF.blit(menu_surf, menu_rect)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_f:
                    pygame.display.toggle_fullscreen()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                for card in card_list:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card.is_clicked = True
                        pygame.mouse.get_rel()
            if event.type == MOUSEBUTTONUP:
                for card in card_list:
                    if card.is_clicked is True:
                        card.is_clicked = False

            if event.type == pygame.MOUSEMOTION:
                for card in card_list:
                    if card.is_clicked is True:
                        card.move_card(pygame.mouse.get_rel())




        DISPLAYSURF.fill(GRAY)

        # clear all the sprites
        render_update_group.clear(DISPLAYSURF, DISPLAYSURF)

        # update all the sprites
        render_update_group.update()

        dirty = render_update_group.draw(DISPLAYSURF)

        pygame.display.update(dirty)

        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for _ in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
