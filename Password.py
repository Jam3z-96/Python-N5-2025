password = input("Please enter your password: ")
while len(password) < 8:
    print("Error, try again with at least 8 characters.")
    password = input("Please enter your password: ")
print("Password accepted.")
