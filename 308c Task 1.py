temps = []
for index in range(1,8):
    message = "Enter temperature " + str(index) + ": "
    thisTemp = float(input(message))
    temps.append(thisTemp)

average_temp = sum(temps) / len(temps)
print("The average temperature is:", average_temp ,"°C")