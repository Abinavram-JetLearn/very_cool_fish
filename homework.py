books = {
    "Physics Book": 100,
    "Chemistry Book": 500,
    "Math Book": 200,
    "English Book": 50,
}
print("Actually The Physics Book is 200")
books["Physics Book"] = 200
books["Drama Book"] = 249
books["Computer Science"] = 1000
while True:
    answer = input("Do you want to buy a book?").lower()
    if answer == "yes":
        while True:
            print("There is:")
            for key in books.keys():
                print(key, books[key])
            answer = input("What book do you want to buy?")
            if answer in books:
                print("Succesfully Bought")
                break
            else:
                print("Book not found please try again")
    else:
        print("ok then bye!")
        break
for key in books.keys():
    print(f"- {key}: {books[key]}.")