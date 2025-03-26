price = [3.99, 5.25, 10.50]
total = 0

for x in range(len(price)):
    total += price[x]

total = round(total, 2)
print('The total cost is: £' + str(total))