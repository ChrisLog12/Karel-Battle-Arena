import pygame
from ai_strategies import AIGreedy
from gui import GameGUI

class KarelBattleArena:
    def __init__(self):
        self.gui = GameGUI()
        self.ai = AIGreedy()
        self.running = True

    def start_game(self):
        print("Starting Karel Battle Arena...")
        self.gui.initialize()
        while self.running:
            self.gui.update()
            self.ai.make_move()
            self.running = self.gui.check_events()

if __name__ == "__main__":
    game = KarelBattleArena()
    game.start_game()
