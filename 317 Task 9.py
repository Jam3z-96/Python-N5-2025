ingredients = {
    "flour (g)": 200,
    "butter (g)": 100,
    "sugar (g)": 80,
    "eggs": 1,
    "chocolate chips (g)": 150,
    "vanilla (tsp)": 1
}
serves_original = 4
serves_new = 6
scaling_factor = serves_new / serves_original
print(f"Scaled ingredients for {serves_new} people:")
for item, amount in ingredients.items():
    scaled = amount * scaling_factor
    if item == "eggs":
        scaled = round(scaled)
    else:
        scaled = round(scaled,2)