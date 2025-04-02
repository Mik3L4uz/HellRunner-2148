"""
File contenente delle classi utili al gioco
"""
import pygame

# Bullet class

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.original_image = pygame.image.load("Models/Objects/Bullet1.png").convert_alpha()
        self.speed = 20
        self.direction = direction
        if self.direction == "left":
            self.image = pygame.transform.flip(self.original_image, True, False)
            self.rect = self.image.get_rect(center=(x - 55, y - 28))
        else:
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(x + 55, y - 28))

    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "left":
            self.rect.x -= self.speed
        if self.rect.right < 0 or self.rect.left > 1500:
            self.kill()
            
# Nemico class
            
class Nemico(pygame.sprite.Sprite):
    def __init__(self, x, y, velocità):
        super().__init__()
        self.original_image = pygame.image.load("Models/Enemy/Bug/Bug1.png").convert_alpha()
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.velocità = velocità + 1
        self.gravity = 1
        self.velocità_y = 0.09
        self.jump_force = 0
        self.on_ground = False
        self.health = 3
        self.hit_timer = 0
        self.direction = "left"  # Direzione iniziale

    def update(self, giocatore_pos, terreno_rect):
        # Movimento orizzontale inseguendo il player
        if giocatore_pos[0] < self.rect.centerx:
            self.rect.x -= self.velocità
            if self.direction != "left":
                self.image = self.original_image.copy()
                self.direction = "left"
        elif giocatore_pos[0] > self.rect.centerx:
            self.rect.x += self.velocità
            if self.direction != "right":
                self.image = pygame.transform.flip(self.original_image, True, False)
                self.direction = "right"

        # Movimento verticale inseguendo il player solo nella fascia (550 - 700)
        if giocatore_pos[1] < self.rect.centery and self.rect.top > 550:
            self.rect.y -= self.velocità
        elif giocatore_pos[1] > self.rect.centery and self.rect.bottom < 700:
            self.rect.y += self.velocità

        # Effetto hit rosso
        if self.hit_timer > 0:
            self.image = self.original_image.copy()
            red_overlay = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            red_overlay.fill((255, 0, 0, 120))  # semi-trasparente rosso
            self.image.blit(red_overlay, (0, 0))
            self.hit_timer -= 1
        else:
            if self.direction == "right":
                self.image = pygame.transform.flip(self.original_image, True, False)
            else:
                self.image = self.original_image.copy()