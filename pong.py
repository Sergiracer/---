from pygame import *
from random import *

font.init()
font1 = font.Font(None, 120)
mixer.init()  
window = display.set_mode((700, 500))
clock = time.Clock()

lose = font1.render('YOU LOSE!', True, (225, 0, 0))

FPS = 60

display.set_caption('Game')
bg = transform.scale(image.load('ajy.jpg'),(700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, image_pl, speed, rect_x, rect_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_pl),(width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y  
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 400:
            self.rect.y += self.speed

player1 = Player("bar1.png", 10, 670, 250, 20, 100)
player2 = Player("bar2.png", 10, 10, 250, 20, 100)
ball = Player("ball.png", 10, 300, 250, 40, 40)
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(bg, (0, 0))
    player1.update1()
    player1.reset()
    ball.reset()
    player2.update2()
    player2.reset()
    clock.tick(FPS)
    display.update()