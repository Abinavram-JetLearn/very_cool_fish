list2 = [
    "nutella",
    "penurts butter",
]
list = [
    "oraneg",
    "blue",
    "red",
    "purple",
    list2
]

print(list[4][1])

list3 = [
    [1,2], [3,4]

]
list4 = [
    [2,1],[4,3]
]
list6 = [
    [2,1],[4,3], [6,5]
]
list7 = [
    [2,1],[4,3], [6,5]
]
list8 = [[0,0],[0,0],[0,0]]
list5 = [
    [0,0],[0,0]
]
print("\n-------")


for i in range(2):
    for j in range(2):
        list5[i][j] = list3[i][j] * list4[i][j]
for i in range(3):
    for j in range(2):
        list8[i][j] = list6[i][j] * list7[i][j]
for item in list5:
    for num in item:
        print(f"|{num}", end="| ",)
    print("\n-------")
for item in list8:
    for num in item:
        print(f"|{num}", end="| ",)
    print("\n-------")