import pygame


class GeneralCard:

    def __init__(self, height, width, attack, defense, health):
        self._height = height
        self._width = width
        self._attack = attack
        self._defense = defense
        self._health = health
