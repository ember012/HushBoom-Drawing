import pygame
from pygame.locals import *

WIDTH = 600
HEIGHT = 700
BLOCK_SIZE = 20

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HushBoom")

rect_color = (150, 150, 150)
offset = [0, 0]
clock = pygame.time.Clock()

# draw grid
grid = []
screen.fill((0, 0, 0))
for x in range(20, WIDTH - 20, BLOCK_SIZE):
    for y in range(20, HEIGHT - 80, BLOCK_SIZE):
        rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, rect_color, rect, 1)
        grid.append(rect)

coloring = (255, 0, 0)

clicking = False

done = False
while not done:
    # buttons on bottom of screen
    stop_button = pygame.Rect((WIDTH / 2) - 40, HEIGHT - 50, 80, 40)
    changeGreen = pygame.Rect(50, HEIGHT - 50, 20, 20)
    changeBlue = pygame.Rect(100, HEIGHT - 50, 20, 20)
    changeRed = pygame.Rect(150, HEIGHT - 50, 20, 20)
    pygame.draw.rect(screen, (255, 0, 0), stop_button)
    pygame.draw.rect(screen, (0, 255, 0), changeGreen)
    pygame.draw.rect(screen, (0, 0, 255), changeBlue)
    pygame.draw.rect(screen, (255, 0, 0), changeRed)

    # check if mouse clicks a rect object
    if clicking:
        posX, posY = pygame.mouse.get_pos()
        for blocks in grid:
            if blocks.collidepoint(posX, posY):
                pygame.draw.rect(screen, coloring, blocks)
            elif stop_button.collidepoint(posX, posY):
                done = True
            elif changeGreen.collidepoint(posX, posY):
                coloring = (0, 255, 0)
            elif changeBlue.collidepoint(posX, posY):
                coloring = (0, 0, 255)
            elif changeRed.collidepoint(posX, posY):
                coloring = (255, 0, 0)

    # button events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()
