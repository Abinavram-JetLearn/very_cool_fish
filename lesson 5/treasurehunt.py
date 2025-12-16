import random, os, math

def print_map():
    os.system("cls")
    print("-----------------------------------------")
    for items in map:
        print("|", end = " ")
        for str in items:
            print(f"{str} |", end = " ")
        print("\n-----------------------------------------")



def game():
    global tr, tc, answer, map
    map = [
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_"],
    ]
    tr = random.randint(0,9)
    tc = random.randint(0,9)
    while True:
        print_map()
        answer = input("Where do you think the treasure is: ")
        if answer.isdigit():
            if not(int(answer[0]) > 9 or int(answer[0]) < 0 or int(answer[1]) > 9 or int(answer[1]) < 0):
                if len(answer) == 2:
                    metresaway = round(math.sqrt(((abs(int(answer[0]) - tr))**2) + ((abs(int(answer[1]) - tc))**2)),2)
                    if int(answer[0]) == tr and int(answer[1]) == tc:
                        print("You Win!")
                        break
                    else:
                        print("Wrong")
                        map[int(answer[0])][int(answer[1])] = "X"
                        print(f"You are {metresaway} metres away")
                        input("Press any key to continue")
                else:
                    print("Wrong you put too much characters")
                    input("Press any key to continue")   
            else:
                print("Wrong you exceeded the boundries or 0 - 6")
                input("Press any key to continue")
        else:
            print("Wrong you cannot type it like that...")
            input("Press any key to continue")

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
            input("press any key to continue")
    if answer == "no":
        break