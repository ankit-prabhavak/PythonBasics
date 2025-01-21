#Problem statement 1:

# a=int(input("Enter a number 1: "))
# b=int(input("Enter a number 2: "))
# c=int(input("Enter a number 3: "))
# d=int(input("Enter a number 4: "))

# if(a>b and a>c and a>d):
#     print("Greatest number entered by you is:",a)

# elif(b>a and b>c and b>d):
#     print("Greatest number entered by you is:",b)

# elif(c>a and c>b and c>d):
#     print("Greatest number entered by you is:",c)

# elif(d>b and d>b and d>c):
#     print("Greatest number entered by you is:",d)    
    
# #Problem statement 2:
# marks1=int(input("Enter marks1:"))
# marks2=int(input("Enter marks2:"))
# marks3=int(input("Enter marks3:"))

# total_percentage=(marks1+marks3+marks2)/3

# if(total_percentage>40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You passed. Congratulations!",total_percentage)
# else:
#     print("You failed. Try again next year!",total_percentage)    

#Problem statement 3:
#spam filter
# p1="Make a lot of money"
# p2="buy this"
# p3="click this"
# p4="subscribe this"

# message=input("Enter your message: ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")    /


# #Problem statement 4:
# name=input("Enter your username: ")

# if(len(name)>):
#     print("valid username")
# else:
#     print("invalid username")

# #Problem statement 5:
# list=["Ankit","Abhinav","Aman","Priyanshu","Virat","Aryan"]

# name=input("Enter your name: ")
# if(name in list):
#     print("Your name is in the list.")
# else:
#     print("Your name is not in the list.")    

#Problem statement 6:
# marks=int(input("Enter your marks: "))

# if(marks<100 and marks>=90):
#     grade="Ex"

# elif(marks<90 and marks>=80):
#     grade="A"

# elif(marks<80 and marks>=70):
#     grade="B"


# elif(marks<70 and marks>=60):
#     grade="C"

# elif(marks>=50 ):
#     grade="F"

# print("Your grade is: ",grade)

#Problem statement 7:

post=input("Enter your post: ")

if("harry" in post.lower()):
    print("This post is about Harry.")
else:
    print("This post is not about Harry.")    