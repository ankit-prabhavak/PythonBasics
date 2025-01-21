#Project 2: Guess the number.


import random
n=random.randint(1,100)

a=-1
Guesses=0
while a!=n:
    a=int(input("Guess the number:"))
    Guesses+=1
    if(a>n):
        print("Too high")

    elif(a<n):
        print("Too low")

print(f"You have  guessed the number {n} in {Guesses} guesses.")



