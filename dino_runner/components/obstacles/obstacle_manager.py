import pygame
import random


from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def generate_obstacle(self):
        num_select = random.randint(0, 1)
        cactus_option = [LARGE_CACTUS, SMALL_CACTUS]
        if num_select == 0:
            return Cactus(cactus_option[random.randint(0,1)])
        if num_select == 1:
            return Bird(BIRD, random.randint(0, 2))
        return


    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle()
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                print("Collision")
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
