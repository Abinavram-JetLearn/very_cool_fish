marks = []
low = []
mid = []
high = []
for i in range(10):
    while True:
        answer = int(input("Give a mark between 1 - 100: "))
        if answer >= 0 and answer <= 100:
            marks.append(answer)
            break
        else:
            print("Not a valid mark")
print(marks)
for i in range(len(marks)):
    if marks[i] < 30:
        low.append(marks[i])
    elif marks[i] > 30 and marks[i] < 66:
        mid.append(marks[i])
    elif marks[i] > 65:
        high.append(marks[i])
print(f"{low}, {mid}, {high}. :)")