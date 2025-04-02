class Franction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        if isinstance(other, Franction):
            return Franction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Franction' and '{}'".format(type(other).__name__))
    
    def __sub__(self, other):
        if isinstance(other, Franction):
            return Franction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Franction' and '{}'".format(type(other).__name__))
        
    def __mul__(self, other):
        if isinstance(other, Franction):
            return Franction(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Franction' and '{}'".format(type(other).__name__))
        
    def __truediv__(self, other):
        if isinstance(other, Franction):
            return Franction(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Franction' and '{}'".format(type(other).__name__))
        

    def __eq__(self, other):
        if isinstance(other, Franction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            raise TypeError("Unsupported operand type(s) for ==: 'Franction' and '{}'".format(type(other).__name__))
        
 
    


f = Franction(3, 4)
print(f)  # Output: 3/4

f1 = Franction(5, 6)
print(f1)  # Output: 5/6

# operations
print(f + f1)  # Output: 38/24
print(f - f1)  # Output: -2/24
print(f * f1)  # Output: 15/24
print(f / f1)  # Output: 18/20
print(f == f1)  # Output: False

print(dir(f))  # This will show all the attributes and methods of the f object





