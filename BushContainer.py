import pygame
import global_data
import random

class BushContainer:
    bushes = []
    bush_width = 50
    bush_height = 110

    def update(self):
        self.create_new_bush()
        self.update_bushes_state()
        self.delete_invisible_bushes()

    def draw(self, screen):
        for bush in self.bushes:
            bush.draw(screen)

    def create_new_bush(self):
        if len(self.bushes) == 0:
            self.bushes.insert(0, Bush(global_data.SCREEN_WIDTH, global_data.GROUND - self.bush_height, self.bush_width, self.bush_height))
            return

        if global_data.SCREEN_WIDTH - self.bushes[0].x > global_data.BUSHES_MIN_INTERVAL:
            numberOfBushes = int((random.random() * 10) % (global_data.MAX_NUMBER_OF_BUSHES + 1)) 

            for i in range(numberOfBushes):
                self.bushes.insert(0, Bush(global_data.SCREEN_WIDTH + i * self.bush_width, global_data.GROUND - self.bush_height, self.bush_width, self.bush_height))

    def update_bushes_state(self):
        for i in range(len(self.bushes)):
            self.bushes[i].x -= global_data.CANVAS_SPEED

    def delete_invisible_bushes(self):
        bushesIndex = len(self.bushes) - 1

        # Удаление с конца
        while bushesIndex > 0:
            if self.bushes[bushesIndex].x + self.bush_width > 0:
                break

            self.bushes.pop()
            bushesIndex -= 1


class Bush:
    x : int
    y : int
    width: int
    height: int

    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def get_x(self):
        return self.x

    def get_collision_box(self):
        return {
            "top_left": {
                "x" : self.x,
                "y" : self.y
            },
            "top_right": {
                "x": self.x + self.width,
                "y" : self.y
            },
            "bottom_left":{
                "x": self.x,
                "y": self.y + self.height
            },
            "bottom_right": {
                "x": self.x + self.width,
                "y": self.y + self.height
            }
        }