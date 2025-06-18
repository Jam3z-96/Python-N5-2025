students = int(input("How many students are in the class?  "))
pizza = round(students / 8)
total_cost = pizza * 12
print("You need to order " + str(pizza) + " pizzas.")
print("The total cost of the pizzas is: $" + str(total_cost))