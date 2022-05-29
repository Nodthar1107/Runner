import pygame
import PlayableCharacter
import Background
import BushContainer
import global_data
import CollisionMediator

pygame.init()

character = PlayableCharacter.PlayableCharacter()
background = Background.Background()
bush_container = BushContainer.BushContainer()
collider = CollisionMediator.CharacterAndBushesCollisionMediator()

screen = pygame.display.set_mode((global_data.SCREEN_WIDTH, global_data.SCREEN_HEIGHT))
pygame.display.set_caption("Google Dino")
gameIsRunning = True
clock = pygame.time.Clock()

while gameIsRunning:

    handleEvent = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if event.type == pygame.KEYDOWN:
            handleEvent = event

    character.update(handleEvent)
    bush_container.update()

    if collider.isCollided(character, bush_container.bushes):
        print("You lose")
        gameIsRunning = False
    
    background.draw(screen)
    character.draw(screen)
    bush_container.draw(screen)

    clock.tick(30)         

    pygame.display.flip()

