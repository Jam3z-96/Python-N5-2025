weights =[]

for index in range(1,6):
    message = "Enter weight " + str(index) + ": "
    weight = float(input(message))
    weights.append(weight)

if 0 <= weight >= 300:
    print("Invalid input. Weight must be between 0g and 300g.")
    
sum = sum(weights)
print("The total amount of food given to the dog over 5 days is :" ,sum)