dictionary = {
    "India": "Dehli",
    "England": "London",
}
response = ""
# Iterate
print(dictionary["India"])
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# Iterable? 1
for key in dictionary:
    print(key,dictionary[key])
# Iterable? 2
for key in dictionary.keys():
    print(key,dictionary[key])
#Iterable? 3
for value in dictionary.values():
    print(value)
#Iterable? 4
for key,value in dictionary.items():
    print(key,value)
# Check
if "Austalia" in dictionary:
    print(True)
else:
    # Update
    print("The Data is not there")
    response = input("Would you like to add it?")
    if response == "yes":
        dictionary["Australia"] = "Canberra"
        print("Ok. Updated")
    else:
        print("Ok. Not updated")
    response = input("Would you lke to delete India?")
    if response == "yes":
        del(dictionary["India"])
        print("Deleted")
    else:
        print("Ok")
    print(dictionary)
    input("Deleting all")
    dictionary.clear()
    print(dictionary)