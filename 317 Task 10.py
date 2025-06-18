unit_cost = 0.15  
standing_charge = 12 
start_reading = float(input("Enter the meter reading at the start of the month: "))
end_reading = float(input("Enter the meter reading at the end of the month: "))
units_used = end_reading - start_reading
cost_of_units = units_used * unit_cost
total_bill = cost_of_units + standing_charge
print("Units used: £" ,units_used)
print("Cost of units: £" ,cost_of_units)
print("Standing charge: £" ,standing_charge)
print("Total bill: £" ,total_bill)