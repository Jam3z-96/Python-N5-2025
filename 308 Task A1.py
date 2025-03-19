list = []
while True:
    score= int(input("Enter your test score: "))
    while score <= -1 or score >= 101:
        print("Error, your score must be between 0 and 100")
        score = int(input("Please enter a valid score: "))

    list.append(score)
    print(list)
