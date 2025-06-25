import random
location = ['Entrance Hall', 'Library', 'Kitchen', 'Garden']
location_description = ['A grand foyer with a crystal chandelier', 'Dusty bookshelves stretch from floor to ceiling', 'Copper pots hang above an old stone hearth', 'Overgrown vines twist around marble statues']
commands = ['N', 'S', 'E', 'W', 'quit', 'help']

print("Welcome to the adventure game!")
name = input("Enter your name: ")
print("Welcome to the mystery mansion, " + name + "!")
print("You have 10 moves to explore the mansion.")

for move in range(10):
    user = input("Enter the direction you want to go in (N, S, E, W), or type 'quit' or 'help': ")
    if user not in commands:
        print("Invalid command. It has to be either N, S, E, W, quit, or help.")
        continue
    if user == 'quit':
        print("You have quit the game.")
        break
    elif user == 'help':
        print("The commands are N, S, E, W, quit, help.")
    elif user in ['N', 'S', 'E', 'W']:
        room = random.randint(0, len(location) - 1)
        print("You have entered the " + location[room] + " - " + location_description[room])