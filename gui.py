import pygame
import matplotlib.pyplot as plt

class GameGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.Surface((300, 300))  # off-screen surface
        self.karel_pos = [50, 50]
        self.beepers = [[100, 100], [200, 150]]  # sample beeper positions

    def initialize(self):
        self.draw_frame()

    def draw_frame(self):
        # Clear screen
        self.screen.fill((255, 255, 255))
        # Draw Karel (blue square)
        pygame.draw.rect(self.screen, (0, 0, 255), (*self.karel_pos, 20, 20))
        # Draw beepers (yellow circles)
        for b in self.beepers:
            pygame.draw.circle(self.screen, (255, 255, 0), b, 10)

        # Convert to numpy array and show inline
        arr = pygame.surfarray.array3d(self.screen)
        plt.imshow(arr)
        plt.axis("off")
        plt.show()

    def move_karel(self, dx, dy):
        self.karel_pos[0] += dx
        self.karel_pos[1] += dy

    def update(self):
        self.draw_frame()

    def check_events(self):
        return True  # always keep running in Colab
