num_of_badges = int(input("Enter the number of badges you want to order: "))
price_per_badge = 25
total_price = num_of_badges * price_per_badge

if num_of_badges > 150:
    total_price *= 0.9

print("Total price: £",total_price,)