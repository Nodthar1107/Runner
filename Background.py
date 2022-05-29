from tkinter import HORIZONTAL
import pygame
import global_data

class Background:
    horizontal_line : int

    def __init__(self):
        self.horizontal_line = global_data.GROUND - 100

    def draw(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0,0,0), (0, self.horizontal_line), (global_data.SCREEN_WIDTH, self.horizontal_line))