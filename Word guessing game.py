import random

words = ["python", "function", "random", "length", "computer", "program", "variable"]
secret_word = random.choice(words)
turns = 5
guessed_correctly = False

print("Welcome to the Word Guessing Game!")
print(f"You have {turns} turns to guess the secret word.")

for turn in range(1, turns + 1):
    guess = input(f"Turn {turn}: Enter your guess: ").lower()
    if guess == secret_word:
        guessed_correctly = True
        break
    else:
        print("Incorrect guess. Try again.")

if guessed_correctly:
    score = round(len(secret_word) / turn, 1)
    print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
    print(f"Your score is: {score}")
else:
    print(f"Sorry, you've run out of turns. The secret word was '{secret_word}'.")
    print("Your score is: 0")