import pgzrun

WIDTH = 1925
HEIGHT = 1000
title = Rect(0,0,WIDTH,100)
title2 = Rect(0,0,WIDTH,100)
question = Rect(12.5,150,1300,100)
ans1 = Rect(25,300,500,300)
ans2 = Rect(25,650,500,300)
ans3 = Rect(812.5,300,500,300)
ans4 = Rect(812.5,650,500,300)
timer = Rect(1400,150, 200,400)
restart = Rect(1400,575,500,400)
skip = Rect(1700,150,200,200)

time_que = 10
game_state = True
titletext = "Hello Welcome to this very cool quiz"
questions = []

def read_question():
    global questions
    file = open("lesson 4\questions.txt", "r")
    for q in file:
        print(q)
        questions.append(q.strip())
    return questions.pop(0).split("|")

cur_question = read_question()

def timer_reduce():
    global time_que, game_state
    if time_que > 0:
        time_que -= 1
    else:
        game_state = False
        time_que = 0

def draw():
    global time_que, titletext, question

    screen.fill("magenta3")
    screen.draw.filled_rect(title,"magenta2")
    screen.draw.filled_rect(title2,"magenta2")
    screen.draw.textbox(f"{titletext}", title, color = "violet red")
    screen.draw.filled_rect(question,"magenta2")
    screen.draw.textbox(cur_question[0], question, color = "violet red")
    screen.draw.filled_rect(ans1,"magenta2")
    screen.draw.textbox(cur_question[1], ans1, color = "violet red")
    screen.draw.filled_rect(ans2,"magenta2")
    screen.draw.textbox(cur_question[2], ans2, color = "violet red")
    screen.draw.filled_rect(ans3,"magenta2")
    screen.draw.textbox(cur_question[3], ans3, color = "violet red")
    screen.draw.filled_rect(ans4,"magenta2")
    screen.draw.textbox(cur_question[4], ans4, color = "violet red")
    screen.draw.filled_rect(skip,"magenta2")
    screen.draw.textbox("Skip", skip, color = "violet red")
    screen.draw.filled_rect(restart,"magenta2")
    screen.draw.textbox("Restart", restart, color = "violet red")
    screen.draw.filled_rect(timer,"magenta2")
    screen.draw.textbox(f"{time_que}", timer, color = "violet red")

def update():
    global titletext
    if game_state == False:
        titletext = "GAME OVER"
    if title.right < 0:
        title.left = WIDTH
    else:
        title.x -= 10

clock.schedule_interval(timer_reduce,1)
pgzrun.go()