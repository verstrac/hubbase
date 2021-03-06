import pygame

from cards.general_card import GeneralCard
from cards.stronghold_card import StrongholdCard
from utils.game_states import GameStates


class CardManager:

    def __init__(self):
        self.my_card = GeneralCard(120, 648)
        self.my_other_card = GeneralCard(200, 648)
        self.stronghold = StrongholdCard(452, 528)
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
                        card.change_card_number(9)
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
