import random
import time

films = ["The odyssey","The lighthouse","The batman","The thing","The drama"]
random_film = random.choice(films)

time.sleep(1)

print("Give a rating for", random_film, "out of 4 (1-4)")
rating = int(input("Please enter your rating"))

if rating == 1:
    print("sorry to hear that")
if rating == 2:
    print("sounds like it was OK then")
if rating == 3:
    print("geat to hear, ill check it out myself")
if rating == 4:
    print("I thought so too, cant wait to see it again")