# Task 2 - (a) Predict and read; (b) Investigate and modify
# (a) Which name and age will not be displayed?
# (b) What two lines of Python code could we use to add 66 year old ‘Edna’ to the arrays?

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

names.append("Edna")
ages.append("66")

for index in range(1,4):
    print(names[index],"is",ages[index])

# (a) - Alice is 25 becuase the first index value is 1 so it misses the values in the first (0) position of both arrays.
# (b) - lines 8 & 9