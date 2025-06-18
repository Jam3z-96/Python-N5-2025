total = []
item_1 = int(input("What is the price of item 1?  "))
item_2 = int(input("What is the price of item 2?  "))
item_3 = int(input("What is the price of item 3?  "))
total.append(item_1)
total.append(item_2)
total.append(item_3)
total_cost = sum(total)
print("The total cost of the items is: £" + str(total_cost))