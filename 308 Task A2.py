print('What is your name?')
name = input()

print('What is your age?')
age = int(input())

while age < 11 or age > 18:
    print('Error, your age must be between 11 and 18')
    age = int(input('Please enter a valid age: '))

else:
    age < 11 and age > 18
    print('Welcome to the talent show, ' + name + '!')
