import random, os, math

def print_map():
    os.system("cls")
    print("---------------------------------------------")
    for items in map:
        print("|", end = " ")
        for str in items:
            print(f"{str} |", end = " ")
        print("\n---------------------------------------------")



def game():
    global tr, tc, answer, map, attempts
    map = [
    ["_","_","_","_","_","_","_","_","_","_","0"],
    ["_","_","_","_","_","_","_","_","_","_","1"],
    ["_","_","_","_","_","_","_","_","_","_","2"],
    ["_","_","_","_","_","_","_","_","_","_","3"],
    ["_","_","_","_","_","_","_","_","_","_","4"],
    ["_","_","_","_","_","_","_","_","_","_","5"],
    ["_","_","_","_","_","_","_","_","_","_","6"],
    ["_","_","_","_","_","_","_","_","_","_","7"],
    ["_","_","_","_","_","_","_","_","_","_","8"],
    ["_","_","_","_","_","_","_","_","_","_","9"],
    ["0","1","2","3","4","5","6","7","8","9","₪"],
    ]
    tr = random.randint(0,9)
    tc = random.randint(0,9)
    attempts = 0
    while True:
        print_map()
        answer = input("Where do you think the treasure is: ")
        if answer.isdigit():
            if len(answer) == 2:
                if not(int(answer[0]) > 9 or int(answer[0]) < 0 or int(answer[1]) > 9 or int(answer[1]) < 0):
                    metresaway = round(math.sqrt(((abs(int(answer[0]) - tr))**2) + ((abs(int(answer[1]) - tc))**2)),3)
                    
                    if int(answer[0]) == tc and int(answer[1]) == tr:
                        print(f"You Win! You took: {attempts} attempt(s)")
                        input("Press any key to continue")
                        break
                    else:
                        print("Wrong")
                        map[int(answer[0])][int(answer[1])] = "X"
                        print(f"You are {metresaway} metres away")
                        input("Press Enter to continue")
                        attempts += 1
                else:
                    print("Wrong you exceeded the boundries or 0 - 9")
                    input("Press Enter to continue")
            else:
                print("Wrong you put too much characters")
                input("Press Enter to continue")   
        else:
            print("Wrong you cannot type it like that... format = xy (x-axis, y-axis)")
            input("Press Enter to continue")

while True:
    game()
    while True:
        os.system("cls")
        answer = input("Do you want to play again? Choice(Yes/No): ").lower().strip()
        if answer == "yes":
            break
        elif answer == "no":
            break
        else:
            print("Try again")
            input("Press Enter to continue")
    if answer == "no":
        break