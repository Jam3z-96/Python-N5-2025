scores = [75, 82, 93, 65, 78]
highest_score = scores[0]
for index in range(1, len(scores)):
    if scores[index] > highest_score:
        highest_score = scores[index]

print(f"The highest score is: {highest_score}")