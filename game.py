from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self):
        pass
    def reset(self):
        pass
class Player(Gamesprite):
    def update_right(self):
        pass
    def update_left(self):
        pass

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))
fon = (200, 255, 255)
window.fill(fon)

game =True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True:
            window.fill(fon)
        display.update()
        clock.tick(FPS)
