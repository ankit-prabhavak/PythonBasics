#Problem statement: Write a program to change degree celcious to farenheit.

def farenheit(degree):
    required=(degree*(9/5))+32
    return required


temperature=float(input("Enter temperature in degree celsius: "))

answer=farenheit(temperature)
print(f"In Farenheit: {round(answer,2)}°F")