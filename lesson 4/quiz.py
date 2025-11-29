import pgzrun

WIDTH = 1925
HEIGHT = 1000
title = Rect(0,0,1925,100)
question = Rect(12.5,150,1300,100)
ans1 = Rect(25,300,500,300)
ans2 = Rect(25,650,500,300)
ans3 = Rect(812.5,300,500,300)
ans4 = Rect(812.5,650,500,300)
timer = Rect(1400,150, 200,400)
restart = Rect(1400,575,500,400)
skip = Rect(1700,150,200,200)
def draw():
    screen.fill("magenta3")
    screen.draw.filled_rect(title,"magenta2")
    screen.draw.filled_rect(question,"magenta2")
    screen.draw.filled_rect(ans1,"magenta2")
    screen.draw.filled_rect(ans2,"magenta2")
    screen.draw.filled_rect(ans3,"magenta2")
    screen.draw.filled_rect(ans4,"magenta2")
    screen.draw.filled_rect(skip,"magenta2")
    screen.draw.filled_rect(restart,"magenta2")
    screen.draw.filled_rect(timer,"magenta2")
def update():
    pass

pgzrun.go()