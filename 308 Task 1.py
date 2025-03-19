percentage = int(input("Enter Percentage: "))
while percentage < 0 or percentage > 100:
    print("Error, % must be between 0 and 100")
    percentage = int(input("Please enter a valid percentage"))
