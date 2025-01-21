a = int(input("Enter the first number: "))
b  = int(input("Enter the second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant for dividing number by zero.")

else:
  print(f"The divison of first by second is: {a/b}")
