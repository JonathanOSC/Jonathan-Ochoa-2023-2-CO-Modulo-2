import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image, position):
        self.type = 1
        super().__init__(image, self.type)
        self.step_index = 0
        self.rect.y = 320 - position*50

    def update(self, game_speed, obstacle):
        super().update(game_speed, obstacle)
        self.run()

    def run(self):
        super().set_image(0 if self.step_index < 5 else 1)
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0