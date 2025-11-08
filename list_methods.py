list = [
    "Banana",
    "Apple",
    "Avacado",
    "Berries",
]
#slicing can be used to put a list's items in another item
print(list[0:2:5])
print(list[::])
print(list[::-1])

#  add/update/remove
list.append("Grapes")
list[2] = "avacadoes"
list.append("mango")

print(list)

animal = list.pop(2)
print(f"animal ate {animal} ")

list.remove("Apple")
print(list)
if "Apple" in list: 
    print("true") 
else: 
    print("false")

for item in list:
    print(f"- <{item}>")
for i in range(len(list)):
    print(f"{i}. {list[i]}")