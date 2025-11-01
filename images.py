import pgzrun
import random

WIDTH = 500
HEIGHT = 600
creep = Actor("creep")
creep.x = 250
creep.y = 300
msg = ""
def draw():
    screen.fill("black")
    screen.draw.text(msg, (0,0), fontsize = 100, color = "red")
    creep.draw()
def update():
    if keyboard.w:
        if creep.y > 0:
            creep.y -= 10
    if keyboard.s:
        if creep.y < 500:
            creep.y += 10
    if keyboard.a:
        if creep.x > 0:
            creep.x -= 10
    if keyboard.d:
        if creep.x < 600:
            creep.x += 10
def on_mouse_down(pos):
    global msg
    if creep.collidepoint(pos):
        creep.image = "creep2"
        msg = "hello!"
    else:
        creep.image = "creep"
        msg = ""
def change_position():
        creep.y = random.randint(0,600)
        creep.x = random.randint(0,500)
clock.schedule_interval(change_position, 0.5)
pgzrun.go()