unit_cost = 0.15  
standing_charge = 12 
start_reading = float(input("Enter the meter reading at the start of the month: "))
end_reading = float(input("Enter the meter reading at the end of the month: "))
units_used = end_reading - start_reading
cost_of_units = units_used * unit_cost
total_bill = cost_of_units + standing_charge
print(f"Units used: {units_used}")
print(f"Cost of units: £{cost_of_units:.2f}")
print(f"Standing charge: £{standing_charge:.2f}")
print(f"Total bill: £{total_bill:.2f}")