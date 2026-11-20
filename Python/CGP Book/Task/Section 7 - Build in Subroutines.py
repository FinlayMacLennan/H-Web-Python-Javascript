#Section 7 - CGP Book
#Built in subroutines

import random

letters = ["a", "bgfgfd", "c", "d"]

def hello(whatever):
    for index in range(len(whatever)):
        if len(whatever[index]) > 4:
            return(whatever)
    return("ahhhhh")

choice = hello(letters)
print(choice)