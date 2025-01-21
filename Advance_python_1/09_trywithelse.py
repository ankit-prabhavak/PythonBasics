try:
    a=int(input("Enter a number: "))

except Exception as e:
    print(e)

else: 
  print("thank you")   # This will run if there is no exception
