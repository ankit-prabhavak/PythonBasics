#if elif else ladder.

age=int(input("Enter your age: "))
#this if is independent.
if(age%2==0):
    print("You have entered an even number.")

#this is another if statement.
if(age>=18):
    print("You are above the age of consent.")
    print("Good for you")
elif(age<0):
    print("You are entering an invalid age.")

elif(age==0):
    print("You are just born.")    

else:
    print("You are below the age of consent.")

print("End of the program")


