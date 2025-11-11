import pgzrun
import random

WIDTH = 800
HEIGHT = 449
HEROSPEED = 5
hero1 = Actor("spidermaan")
hero2 = Actor("supersman")
hero1score = 0
hero2score = 0
hero1colide = False
hero2colide = False
items =  [

]

for i in range (10):
    item = Actor("item")
    item.x = random.randint(100,700)
    item.y = random.randint(10,439)
    items.append(item)

def draw():
    screen.blit("background", (0,0))
    hero1.draw()
    for item in items:
        item.draw()
    hero2.draw()
    screen.draw.text(f"Superman score: {hero1score}", (0,0), fontsize = 40, color = "red")
    screen.draw.text(f"Spiderman score: {hero2score}", (500,0), fontsize = 40, color = "blue")
def update():
    global hero1score, hero2score, hero1colide, hero2colide
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

    if keyboard.w or keyboard.a or keyboard.s or keyboard.d or keyboard.q or keyboard.e:
        if hero1.colliderect(hero2):
            print("Hero1 touching Hero2")
            hero1colide = True
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
    
    if keyboard.j or keyboard.l or keyboard.k or keyboard.i or keyboard.u or keyboard.o:
        if hero2.colliderect(hero1):
            print("Hero2 touching Hero1")
            hero2colide = True
    
    for item in items:
        if item.colliderect(hero1):
            hero1score += 1
            items.remove(item)
        if item.colliderect(hero2):
            hero2score += 1
            items.remove(item)

    if hero1colide == True:
        hero1score = 0
        hero1colide = False
    if hero2colide == True:
        hero2score = 0
        hero2colide = False
pgzrun.go()