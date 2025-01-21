#Problem statement: Write a python function which converts inches to cm.


def inches_cms(inch):
    return inch*2.54

inch=float(input("Enter the measurement in inches: "))
req=inches_cms(inch)

print(f"Measurement in cm is: {round(req,2)} cm.")
