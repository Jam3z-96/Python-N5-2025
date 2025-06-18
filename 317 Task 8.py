scored = int(input("How many goals were scored? "))
conceded = int(input("How many goals were conceded? "))
played = int(input("How many games were played? "))
difference = scored - conceded
overall = conceded / played
if played > 10:
    average = scored / played
    print("The average goals scored per game is: " + str(average))
print("The goal difference is: " + str(difference))