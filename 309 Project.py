temperatures = []
for i in range(5):
        while True:
            try:
                temp = float(input(f"Enter temperature {i + 1} between -20 and +50°C: "))
                if -20 <= temp <= 50:
                    temperatures.append(temp)
                    break
                else:
                    print("Invalid input. Temperature must be between -20 and +50°C.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

print("Temperatures entered:")
for temp in temperatures:
    print(f"{temp} °C")

total = sum(temperatures)
average_temp = total / len(temperatures)
print(f"The average temperature is: {round(average_temp, 2)} °C")
