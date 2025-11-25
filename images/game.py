import pgzrun
import random

WIDTH = 512
HEIGHT = 544
player = Actor("ship")
player.pos = 256, 252
enemies = []
enemyImages = ["greenenemy", "blueenemy", "redenemy", "greyenemy"]
game = True
timer = 0
red_count = 0
player_charges = 0
player_life = 10
attackmode = False
explosions = []
explosion_frame = ["explosion1", "explosion2", "explosion3", "explosion4", "explosion5", "explosion6"]

# green enemy - normal
# blue enemy - fast one
# red enemy - durable one (touch it and it spawns again only once)
# grey enemy - goes at a random speed (10, -10)

def enemycreator():
    for i in range(1):
        enemy = Actor(random.choice(enemyImages))
        if enemy.image == "greenenemy":
            enemy.pos = (95,110)
        if enemy.image == "blueenemy":
            enemy.pos = (417,110)
        if enemy.image == "redenemy":
            enemy.pos = (95,434)
        if enemy.image == "greyenemy":
            enemy.pos = (417,434)
        enemies.append(enemy)

def explosionbomb():
    global explosion, explosion_frame
    for explosion in explosions:
        if explosion.image == "explosion1":
            explosion.image = "explosion2"
        elif explosion.image == "explosion2":
            explosion.image = "explosion3"
        elif explosion.image == "explosion3":
            explosion.image = "explosion4"
        elif explosion.image == "explosion4":
            explosion.image = "explosion5"
        elif explosion.image == "explosion5":
            explosion.image = "explosion6"
        elif explosion.image == "explosion6":
            explosions.remove(explosion)
    clock.schedule(explosionbomb, 0.1)
clock.schedule(explosionbomb, 0.1)
        


def draw():
    global timer, explosions, player_life, player_charges, enemies, attackmode, red_count

    screen.blit("map", (0,0))
    player.draw()
    screen.draw.text(f"Charges: {player_charges}", (WIDTH/2 -40, 50))
    screen.draw.text(f"Lives: {player_life}", (WIDTH/2 -40, 75))
    if game == True:
        for enemy in enemies:
            enemy.draw()
            if enemy.image == "greenenemy":
                animate(enemy, pos = player.pos, angle = enemy.angle_to(player.pos) - 90, duration = 2,)
            elif enemy.image == "blueenemy":
                animate(enemy, pos = player.pos, angle = enemy.angle_to(player.pos) - 90, duration = 0.25,)
            elif enemy.image == "redenemy":
                animate(enemy, pos = player.pos, angle = enemy.angle_to(player.pos) - 90, duration = 2,)
            elif enemy.image == "greyenemy":
                animate(enemy, pos = player.pos, angle = enemy.angle_to(player.pos) - 90, duration = random.uniform(0.5,2),)
            if enemy.colliderect(player):
                if attackmode == False:
                    player_life -= 1
                    explosion =  Actor("explosion1")
                    explosions.append(explosion)
                    explosion.pos = enemy.pos
                    enemies.remove(enemy)
                else:
                    if enemy.image == "redenemy":
                        if red_count >= 2:
                            player_charges += 1
                            explosion =  Actor("explosion1")
                            explosions.append(explosion)
                            explosion.pos = enemy.pos
                            enemies.remove(enemy)
                            red_count = 0
                        else:
                            enemy.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
                            red_count += 1
                            animate(enemy, pos = player.pos, angle = enemy.angle_to(player.pos) - 90, duration = 2,)
                    else:
                        player_charges += 1
                        explosion =  Actor("explosion1")
                        explosions.append(explosion)
                        explosion.pos = enemy.pos
                        enemies.remove(enemy)
        
        timer += 1
        if timer > 80:
            enemycreator()
            timer = 0
        for explosion in explosions:
            explosion.draw()
def update():
    global player_life, player_charges, enemies, attackmode, explosions        
    if player_charges >= 10:
        player_charges = 0
        player_life += 1
    
def attackend():
    global attackmode
    attackmode = False

def on_mouse_down(pos):
    global attackmode
    animate(player, angle = player.angle_to(pos) - 90, duration = 0.01)
    animate(player, pos = pos, duration = 0.5, tween = "accel_decel", on_finished = attackend)
    if attackmode == False:
        attackmode = True

pgzrun.go()