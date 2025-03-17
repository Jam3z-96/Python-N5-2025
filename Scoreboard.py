home = 0
away = 0
period = 1

print("This is a hockey scoreboard!")
print("Pressing 'h' will add to the home team score.")
print("Pressing 'a' will add to the away team score.")
print("Pressing 'x' will go to the next period.")

while period < 4:
    print("HT:",home,)
    print("AT:",away,)
    print("Period:",period,)
    key = input()
    if key == "h":
        home += 1
    elif key == "a":
        away += 1
    elif key == "x":
        period += 1

print("Game Over!")
print("Final HT:",home,)
print("Final AT:",away,)
print("Final Period:",period - 1,)