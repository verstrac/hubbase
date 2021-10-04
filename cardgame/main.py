import sys
import pygame
from pygame.locals import *

from cardgame.cards.GeneralCard import GeneralCard


WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
GRAY = (185, 185, 185)
FPS = 60


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), RESIZABLE)
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    while True:
        run_game()

def run_game():
    render_update_group = pygame.sprite.RenderUpdates()
    GeneralCard.containers = render_update_group
    my_card = GeneralCard(32, 0)

    while True:
        checkForQuit()

        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if event.key == K_f:
                    pygame.display.toggle_fullscreen()

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
    for event in pygame.event.get(QUIT):  # get all the QUIT events
        terminate()  # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP):  # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate()  # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event)  # put the other KEYUP event objects back


if __name__ == '__main__':
    main()
