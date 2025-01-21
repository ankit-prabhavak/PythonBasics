#Problem statement: Write a program to update score in using a game function().
import random

def game():
     print("You are playing a game..")
     score=random.randint(1,101)

     with open("lucky.txt") as f:
          hiscore=f.read()
          if(hiscore != ""):
               hiscore=int(hiscore)
          else:
               hiscore=0
    
     print(f"Your score is: {score}")

     if(score>hiscore):
          with open("lucky.txt","w") as f:
               f.write(str(score))


game()