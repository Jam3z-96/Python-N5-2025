overdue = int(input("How many days overdue is the book?  "))
fine_per_day = 0.50
total_fine = overdue * fine_per_day
if total_fine > 5:
    total_fine = total_fine + 2.00 
print("The total fine for the overdue book is: £" + str(total_fine))