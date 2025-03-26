names = ['James', 'Ali', 'Frazer', 'John', 'Michael', 'David', 'Peter', 'Paul', 'George', 'Ringo', 'Stuart', 'Pete', 'Brian', 'Roger', 'John', 'Keith', 'Mick', 'Charlie', 'Bill', 'Ronnie', 'Ian', 'Jimmy', 'Robert', 'John']
highest_names = len(names[0])
pos = 0
for index in range(1,len(names)):
    if len(names[index]) > highest_names:
        highest_names = len(names[index])
        pos = index

print(f"{names(pos)} has the longest name with {highest_names} characters.")