import pygame
import sys

class RotatingSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, pos):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def update(self, clockwise=True):
        if clockwise:
            self.angle -= 1 
        else:
            self.angle += 1  

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Вращение спрайта")
clock = pygame.time.Clock()

sprite = RotatingSprite("sprite.png", (300, 200))
all_sprites = pygame.sprite.Group(sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(clockwise=True) 
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
=======
import pygame
import sys


class RotatingSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, pos):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def update(self, clockwise=True):
        if clockwise:
            self.angle -= 1  
        else:
            self.angle += 1 

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Вращение спрайта")
clock = pygame.time.Clock()


sprite = RotatingSprite("sprite.png", (300, 200))
all_sprites = pygame.sprite.Group(sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(clockwise=True)
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

