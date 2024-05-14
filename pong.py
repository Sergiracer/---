from pygame import *
from random import *

font.init()
lose1 = font.Font(None, 60)
lose2 = font.Font(None, 60)
restart = font.Font(None, 30)
mixer.init()  
window = display.set_mode((700, 500))
clock = time.Clock()

lose1 = lose1.render('PLAYER 1 LOSE!', True, (225, 0, 0))
lose2 = lose2.render('PLAYER 2 LOSE!', True, (225, 0, 0))
restart = restart.render('Press SPACE to retart', True, (225, 0, 0))
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
ball = GameSprite("ball.png", 10, 300, 250, 40, 40)

sp_x = 3
sp_y = 3
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finish = False
                sp_x *= -1
                ball.rect.x = 200
    if not finish:
        window.blit(bg, (0, 0))
        player1.update1()
        player1.reset()
        ball.reset()
        player2.update2()
        player2.reset()
        ball.rect.x += sp_x
        ball.rect.y += sp_y
        if ball.rect.y <= 0 or ball.rect.y >= 460:
            sp_y *= -1
        if sprite.collide_rect(ball, player1) == True or sprite.collide_rect(ball, player2) == True:
            sp_x *= -1
        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1, (185, 220))
            window.blit(restart, (220, 465))
        if ball.rect.x > 660 :
            finish = True
            window.blit(lose2, (185, 220))
            window.blit(restart, (220, 465))
    
    clock.tick(FPS)
    display.update()
