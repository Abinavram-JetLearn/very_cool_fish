import pgzrun
import random

WIDTH = 512
HEIGHT = 544
player = Actor("ship")
player.pos = 95,434
enemies = []
enemyImages = ["greenenemy", "blueenemy", "redenemy", "greyenemy"]

def enemycreator():
    enemy = Actor(random.choice(enemyImages))
    if enemy.image == "greenenemy":
        enemy.pos = (95,110)
    if enemy.image == "blueenemy":
        enemy.pos = (417,110)
    if enemy.image == "redenemy":
        enemy.pos = (95,434)
def draw():
    screen.blit("map", (0,0))
    player.draw()

def update():
    pass

def on_mouse_down(pos):
    animate(player, pos = pos, duration = 0.5, tween = "accel_decel",)

    print(pos)
pgzrun.go()