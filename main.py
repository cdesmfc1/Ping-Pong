from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def move_right(self):
        keys = key.get_pressed()
        if keys[K_UP] :
            self.rect.y -= self.speed
        if keys[K_DOWN] :
            self.rect.y += self.speed
    def move_left(self):
        keys = key.get_pressed()
        if keys[K_w] :
            self.rect.y -= self.speed
        if keys[K_s] :
            self.rect.y += self.speed    
        







#game scene:
back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
text_score = font.render('Score', True, (180, 0, 0))

Player1_score = 0
Player2_score = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.move_right()
        racket2.move_left()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        value_score = font.render(str(Player1_score) + " " + str(Player2_score), True, (122, 185, 85))
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
           speed_x*=-1
        if ball.rect.y < 0 or ball.rect.y > win_height - 50:
            speed_y*=-1
        if ball.rect.x < 0:
            
            Player2_score += 1
            ball.rect.x = 300
        if ball.rect.x > 600:
            Player1_score += 1
            ball.rect.x = 300
        if Player1_score >= 3:
            window.blit(lose2, (200, 200))
            finish = True
        elif Player2_score >= 3:
            window.blit(lose1, (200, 200))
            finish = True
        window.blit(text_score, (275, 50))
        window.blit(value_score, (275, 100))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)