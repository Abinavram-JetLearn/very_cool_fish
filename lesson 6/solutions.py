import math

#Solution 1

plist = [0,1,2,3,4,5]

x = 0
for item in plist:
    if item % 2 == 0:
        print(item)
        x += 1
print(f"There are {x} even numbers")

#Soulution 2

list2 = ["red", "orange", "green"]

answer = input("Say something and i Will tell you if it is in my list")

if answer in list2:
    print("yes it is in it")
else:
    print("no it is not")

# Solution 3

ptuple = (43,96,217,43,34,34,98,100)

answer = input()
x = 0
for item in ptuple:
    if int(answer) == item:
        x+=1
print(f"There is {x} numbers like this in the tuple")

# Solution 4

t = (1,2,3)
l = list(t)
l[1] = 4
l = tuple(l)
print(l)

# Solution 5
list3 = [1,1,2,3,4,5,5,6,7,8,9,9,0]

list3 = set(list3)
list3 = list(list3)
print(list3)