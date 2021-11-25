from enum import unique, Enum


@unique
class GameStates(Enum):
    MENU = 'MENU'
    GAME = 'GAME'
