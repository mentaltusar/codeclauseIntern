import random
import os

SCORE = 0
LIFE = 5
gen_number = random.randint(0, 9)
print("________________Welcome to Number Guessing game__________________")
print(f"Your Score is : {SCORE}")
print(f"Life remains : {LIFE}")
while LIFE != 0:

    number = int(input("Guess the Number (Between 0 & 9) :"))

    if number == gen_number:
        print(f"Hoh!! you got it ,it's {number}")
        SCORE += 1
        LIFE = 5
        print("_______________")
        print(f"your Score is : {SCORE}")
        print(f"Your Life : {LIFE}")

        gen_number = random.randint(0, 9)
    elif number > gen_number:
        print("it's Too High .")
        LIFE -= 1
        print(f"Your Score is : {SCORE}")
        print(f"Remaining Life : {LIFE}")
    else:
        LIFE -= 1
        print("it's Too low")
        print(f"Your Score is : {SCORE}")
        print(f"Remain Life : {LIFE}")
