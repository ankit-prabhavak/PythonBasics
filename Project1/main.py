#Project: snake , water and gun.

import random

computer=random.choice([1,-1,0])

print("Choices:: [ s:SNAKE | w:WATER | g:GUN ]")

user=input("Enter your choice: ")

choice={"snake":1,"water":-1,"gun":0}
reverse_choice={1:"Snake",-1:"Water",0:"Gun"}

you=choice[user]

print(f"You choosed: {reverse_choice[you]}\nComputer choosed: {reverse_choice[computer]}")

if(you==computer):
    print("It's a draw!")
else:
    if(computer==1 and you==-1):
        print("You lost!")
    elif(computer==1 and you==0):
        print("You won. Congratulations!")
    elif(computer==-1 and you==1):
        print("You won. Congratulations!")
    elif(computer==-1 and you==0):
        print("You lost!")
    elif(computer==0 and you==1):
        print("You lost!")
    elif(computer==0 and you==-1):
        print("You won. Congratulations!")
    else:
        print("something went wrong!")

