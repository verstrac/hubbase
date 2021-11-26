from cards.GeneralCard import GeneralCard


class CardManager:

    def __init__(self):
        self.my_card = GeneralCard(32, 0)
        self.my_other_card = GeneralCard(64, 64)
        self.card_list = [self.my_card, self.my_other_card]

    def get_card_list(self):
        return self.card_list

