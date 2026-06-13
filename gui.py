import pygame
import matplotlib.pyplot as plt

class GameGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.Surface((300, 300))  # off-screen surface
        self.karel_pos = [50, 50]

    def initialize(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 255), (*self.karel_pos, 20, 20))

    def update(self):
        # Draw Karel again (blue square)
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 0, 255), (*self.karel_pos, 20, 20))

        # Convert to numpy array and show inline
        arr = pygame.surfarray.array3d(self.screen)
        plt.imshow(arr)
        plt.axis("off")
        plt.show()

    def move_karel(self, dx, dy):
        self.karel_pos[0] += dx
        self.karel_pos[1] += dy

    def check_events(self):
        return True  # always keep running in Colab
