import sys
import pygame
from pygame.math import Vector2
import random


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

class Block:
    def __init__(self):
        pass

    def draw_lock(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0, 1)

    def draw_block(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            # create a rect
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # draw the rectangle
            pygame.draw.rect(screen, (180, 116, 114), block_rect)

    def move_block(self):
        for block in self.body:
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            body_copy = self.body[:]  # we will copy only first two elements
            body_copy.insert(0,body_copy[0] + self.direction)  # insert new element right before at the start f the list
            self.body = body_copy[:]

class MAIN_GAME_LOGIC:
    def __init__(self):
        self.new_block = Block()

    def update(self):
        self.new_block.move_block()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            # Controlling snake direction
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0)
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)