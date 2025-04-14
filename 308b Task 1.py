total = 0
monthly_totals = []
for i in range(12):
    saving = float(input(f"Enter your month {i + 1} savings (£): "))
    total += saving
    monthly_totals.append(total)
    print(f"Your running totals for month {i + 1} is : £{total}")
print((f"Your savings for the year is : £{total}"))
