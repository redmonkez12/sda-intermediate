import pygame


class Player:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/player_object.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.move_left = False
        self.move_right = False
        self.speed = 3

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.speed

        if self.move_right and self.screen_rect.right > self.rect.right:
            self.rect.x += self.speed
