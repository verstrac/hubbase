import pygame

from cards.GeneralCard import GeneralCard
from menu.menu_manager import MenuManager
from state.game_state_manager import GameStateManager
from utils.game_states import GameStates

class CardManager:

    def __init__(self):
        self.my_card = GeneralCard(32, 0)
        self.my_other_card = GeneralCard(64, 64)
        self.card_list = [self.my_card, self.my_other_card]

    def get_card_list(self):
        return self.card_list

    def card_event(self, events, menu_rect, game_state_manager):
        for event in events.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
                for card in self.card_list:
                    if card.rect.collidepoint(pygame.mouse.get_pos()):
                        card.is_clicked = True
                        pygame.mouse.get_rel()
                    if menu_rect.collidepoint(pygame.mouse.get_pos()):
                        game_state_manager.set_game_state(GameStates.MENU)
            if event.type == pygame.MOUSEBUTTONUP:
                for card in self.card_list:
                    if card.is_clicked is True:
                        card.is_clicked = False
            if event.type == pygame.MOUSEMOTION:
                for card in self.card_list:
                    if card.is_clicked is True:
                        card.move_card(pygame.mouse.get_rel())