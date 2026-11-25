# Task 3

# Write a program that will ask the user for their name and a test mark out of 100.
# This should be looped five times and the names and marks should be stored in separate arrays. 
# Print out the contents of the names and the marks arrays.

names = []
test_mark = []

for i in range(5):
    print("Hello please input yout name and your test mark out of 100")
    name = str(input("Please enter your name"))
    mark = int(input("Please enter your test mark"))

    while mark > 100 or mark < 0:
        print("Invaild mark please enter another one (Must be between 0 and 100)")
        mark = int(input("Please enter your test mark"))

    names.append(name)
    test_mark.append(mark)

print(names)
print(test_mark)