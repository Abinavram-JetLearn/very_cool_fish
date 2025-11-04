import pgzrun

WIDTH = 800
HEIGHT = 449
HEROSPEED = 5
hero1 = Actor("supersman")
hero2 = Actor("spidermaan")
def draw():
    screen.blit("background", (0,0))
    hero1.draw()
    hero2.draw()
def update():
    if keyboard.w:
        hero1.y -= 5
    if keyboard.s:
        hero1.y += 5
    if keyboard.a:
        hero1.x -= 5
    if keyboard.d:
        hero1.x +=5
    if keyboard.q:
        if hero1.angle < 90:
            hero1.angle += 5
    if keyboard.e:
        if hero1.angle > -90:
            hero1.angle -= 5
    if keyboard.i:
        hero2.y -= 5
    if keyboard.k:
        hero2.y += 5
    if keyboard.j:
        hero2.x -= 5
    if keyboard.l:
        hero2.x +=5
    if keyboard.u:
        if hero2.angle < 90:
            hero2.angle += 5
    if keyboard.o:
        if hero2.angle > -90:
            hero2.angle -= 5
pgzrun.go()