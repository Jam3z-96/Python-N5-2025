weights = []
for i in range(5):
        while True:
            try:
                weight = float(input(f"Enter weight of dog food {i + 1} between 0kg and 300kg: "))
                if 0 <= weight <= 300:
                    weights.append(weight)
                    break
                else:
                    print("Invalid input. Weight must be between 0kg and 300kg.")
            except ValueError:
                print("Invalid input. Please enter a valid weight.")

print("Weights entered:")
for weight in weights:
    print(f"{weight} kg")

total = sum(weights)
average_weight = total / len(weights)
print(f"The average weight is: {round(average_weight, 2)} kg")
