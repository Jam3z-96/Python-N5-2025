homeHT = int(input("Enter the half time score for the home team: "))
awayHT = int(input("Enter the half time score for the away team: "))
homeFT = int(input("Enter the full time score for the home team: "))
awayFT = int(input("Enter the full time score for the away team: "))
noGoalsScored = (homeFT + awayFT) - (homeHT + awayHT)
print("The number of goals scored after the half time break was: "+str(noGoalsScored))