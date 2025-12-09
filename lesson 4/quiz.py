import pgzrun, random

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
score = 0
answerboxes = [ans1, ans2, ans3, ans4]

time_que = 10
game_state = True
titletext = "Hello Welcome to this very cool quiz"
questions = []

def read_question():
    global questions
    file = open("lesson 4/questions.txt", "r", encoding = "utf-8")
    for q in file:
        questions.append(q.strip())
    random.shuffle(questions)
    q = questions.pop(0).split("|")
    return q

cur_question = read_question()

def timer_reduce():
    global time_que, game_state, cur_question
    if time_que > 0:
        time_que -= 1
    else:
        game_state = False
        time_que = 0
        cur_question = [f"Game Over You scored {score} point(s)!", "-", "-", "-", "-", "-", 5]
        time_que = 0

def draw():
    global time_que, titletext, question, score

    screen.fill("magenta3")
    screen.draw.filled_rect(title,"magenta2")
    screen.draw.filled_rect(title2,"magenta2")
    screen.draw.textbox(f"{titletext}, Score: {score}", title, color = "violet red")
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
def on_mouse_down(pos):
    global time_que, cur_question, score, questions, game_state
    index = 1
    if game_state == True:
        for box in answerboxes:
            if box.collidepoint(pos):
                if index == int(cur_question[5]):
                    score += 1
                    if questions:
                        cur_question = read_question()
                        time_que = 10
                else:
                    cur_question = [f"Game Over You scored {score} point(s)!", "-", "-", "-", "-", "-", 5]
                    time_que = 0
            index += 1
    if skip.collidepoint(pos):
        if questions:
            if game_state == True:
                cur_question = read_question()
                time_que = 10
                if score > 0:
                    score -= 1
                else:
                    cur_question = [f"Game Over You (skipped) scored {score} point(s)!", "-", "-", "-", "-", "-", 5]
                    time_que = 0
    if restart.collidepoint(pos):
        questions = []
        cur_question = read_question()
        score = 0
        time_que = 10
        game_state = True

clock.schedule_interval(timer_reduce,1)
pgzrun.go()