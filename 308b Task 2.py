total = 0
test_scores_running = []
for i in range(5):
    scores = float(input(f"Enter score {i + 1}: "))
    total += scores
    test_scores_running.append(total)
    print(f"Your running totals for score {i + 1} is : {total}")
print((f"Your total score is : {total}"))