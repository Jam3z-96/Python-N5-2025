import random

rightnumber = random.randint(1,10)
guess = 1
number  =int(input("Guess a number from 1 to 10: "))
while (guess < 3) and (number != rightnumber):
    print("Not right. Try again.")
    number = int(input("Guess a number 1 to 10: "))
    guess = guess + 1
if number == rightnumber:
    print("Well done!")