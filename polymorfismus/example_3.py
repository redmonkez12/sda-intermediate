from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def draw(self):
        pass


class Pacman(Entity):
    def draw(self):
        print("Drawing pacman...")


class Ghost(Entity):
    def draw(self):
        print("Drawing Ghost")


class Flower(Entity):
    def draw(self):
        print("Drawing Ghost")


sprites = [
    Pacman(),
    Ghost(),
    Ghost(),
    Ghost(),
    Ghost(),
    Flower(),
    Flower(),
]


class Game:
    def init(self, entities: list[Entity]):
        # draw game board...
        for sprite in sprites:
            sprite.draw()  # nezajimaji me konkretni implementace ve tride
            # ale jen to jak ta metoda vypada
