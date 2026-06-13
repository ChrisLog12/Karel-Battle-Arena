import pygame

class GameGUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Karel Battle Arena")

    def initialize(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def update(self):
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
