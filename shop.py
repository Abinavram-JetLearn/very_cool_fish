sell = {
    "Red Cup": 10,
    "Orange Cup": 10,
    "Yellow Cup": 15,
    "Green Cup": 5,
    "Blue Cup": 20,
    "Indigo Cup": 15,
    "Violet Cup": 90,
    "Diamond Cup": 590,
}
inventory = {}
money = 1000
response = ""

print("✨ Welcome to the Cup Shop! ✨")
print("You can say: 'Buy item', 'Check Shop', 'Check Inventory, 'Sell Item', 'Exit Shop and Live life'.")
print("")
while True:
    print(f"You have {money} coins")
    response = input("Select one of the options: ").lower()
    if response == "check shop":
        for key in sell.keys():
            print(key + " : " +str(sell[key]))
    elif response == "check inventory":
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            for key in inventory.keys():
                print(key + " : " + str(inventory[key]))
    elif response == "sell item":
        if inventory == {}:
            print("Nothing to sell?")
        else:
            while True:
                for key in inventory.keys():
                    print(key, " : ( ", sell[key], " coins).")
                response = input("Which item to sell")
                if response in inventory and response in sell:
                    money += sell[response]
                    del(inventory[response])
                    print(f"Succesfully sold! Here is {sell[response]} money!")
                    break
                else:
                    print(" You can only sell items that are in your inventory. Try again")
    elif response == "buy item":
        for key in sell.keys():
            print(key, " : ", str(sell[key]))
        response = input("Which Item?")
        if response in sell and money >= sell[response]:
            if response in inventory:
                inventory[response] += 1
            else:
                inventory[response] = 1
            print("Item successfully added to inventory")
            money -= sell[response]
        else:
            print("Invalid Purchase, Card Declined")
            print(f"You need {sell[response] - money} more coins to buy.")
    elif response == "exit shop and live life":
        print("Go and live life")
        break
    else:
        print("Invalid Response")
    print("")