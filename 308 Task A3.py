valid_houses = ["Stuart", "Forbes", "Douglas", "Gordon"]

print('What is your name?')
name = input()

print('What is your school house?')
house = input()

while house not in valid_houses:
    print("Error, your house must be either Stuart, Forbes, Douglas or Gordon")
    house = input("Please enter a valid house: ")

user = [name, house]
print(f'Name: {user[0]}')
print(f'House: {user[1]}')