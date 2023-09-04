import pygame
import sys
# sys.exit()
from settings import Settings
from player import Player
from bullet import Bullet
from alien import Alien


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))

        self.player = Player(self)

        self.bullet_group = pygame.sprite.Group()
        self.alien_group = pygame.sprite.Group()

        self._create_fleet()

        pygame.display.set_caption("Super hra!!!")
        self.clock = pygame.time.Clock()

    def _check_ufoun_edges(self):
        for alien in self.alien_group.sprites():
            if alien._check_edges():
                self._change_ufoun_direction()
                break

    def _change_ufoun_direction(self):
        for alien in self.alien_group.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        new_ufo = Alien(self)
        # ufo_width = new_ufo.rect.width
        ufo_width, ufo_height = new_ufo.rect.size

        # current_x = ufo_width
        current_x, current_y = ufo_width, ufo_height

        # while current_x < self.settings.screen_width:
        while current_y < (self.screen.get_height() - 3 * ufo_height):
            while current_x < (self.screen.get_width() - 2 * ufo_width):
                new_ufo = Alien(self)
                self.alien_group.add(new_ufo)
                print(current_x)

                new_ufo.x = current_x
                new_ufo.rect.x = current_x
                new_ufo.rect.y = current_y

                current_x += 2 * ufo_width

            current_x = ufo_width
            current_y += 2 * ufo_height


        # self.alien_group.add()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right = True
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                    elif event.key == pygame.K_q:
                        sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right = False

                elif event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            self.bullet_group.update()
            self.player.update()
            self._update_bullet()

            self._check_ufoun_edges()
            self.alien_group.update()

            for bullet in self.bullet_group.sprites():
                bullet.draw_bullet()

            self.player.blit_me()
            self.alien_group.draw(self.screen)
            pygame.display.flip()

            for bullet in self.bullet_group.copy():
                if bullet.rect.bottom <= 0:
                    self.bullet_group.remove(bullet)

            self.clock.tick(60)

    def _fire_bullet(self):
        if len(self.bullet_group) < self.settings.bullet_count:
            new_bullet = Bullet(self)
            self.bullet_group.add(new_bullet)

    def _update_bullet(self):
        pygame.sprite.groupcollide(self.bullet_group, self.alien_group, True, True)

if __name__ == "__main__":
    game = Game()
    game.run()

