from utils.game_states import GameStates


class GameStateManager:

    def __init__(self):
        self.state = GameStates.GAME

    def get_current_state(self):
        return self.state

    def set_game_state(self, state):
        self.state = state
