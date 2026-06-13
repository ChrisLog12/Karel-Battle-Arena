import time
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
            self.gui.move_karel(10, 0)  # move right each step
            self.gui.update()
            self.ai.make_move()
            time.sleep(1)  # pause so you can see frames
            self.running = self.gui.check_events()

if __name__ == "__main__":
    game = KarelBattleArena()
    game.start_game()
