import pygame
import global_data
import Rectangle

class PlayableCharacter:
    x : int
    y : int
    width : int
    height : int

    collision_padding : int
    
    jumping_speed: int
    current_jumping_speed: int

    isJumping : bool

    def __init__(self):
        self.width = 100
        self.height = 140
        self.x = 20
        self.y = global_data.GROUND - self.height
        self.jumping_speed = 60
        self.current_jumping_speed = self.jumping_speed
        self.isJumping = False

        self.collision_padding = 20

    def update(self, event):
        self.update_state(event)
        self.update_position()

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def update_animation(self):
        if self.isJumping:
            return

    def update_position(self):
        if not self.isJumping:
            return

        print(global_data.GROUND, self.y)

        self.y -= self.current_jumping_speed
        self.current_jumping_speed -= global_data.GRAVITY_CONSTANT


        if self.y + self.height >= global_data.GROUND:
            self.y = global_data.GROUND - self.height
            self.current_jumping_speed = self.jumping_speed
            self.isJumping = False
        

    def update_state(self, event):
        if event is None:
            return

        if event.key == pygame.K_SPACE:
            self.isJumping = True

    def get_collision_box(self):
        return Rectangle.Rectangle(())