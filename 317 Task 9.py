names = ['Flour', 'Butter', 'Sugar', 'Eggs', 'CC', 'Vanilla']
orig = [100, 100, 100, 2, 50, 5]

scale = 6/4

for i in range(len(orig)):
    new_amount = orig[i] * scale
    print(names[i], ":", new_amount)