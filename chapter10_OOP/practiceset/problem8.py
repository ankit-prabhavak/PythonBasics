class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Fraction' and '{}'".format(type(other).__name__))
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Fraction' and '{}'".format(type(other).__name__))
        
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Fraction' and '{}'".format(type(other).__name__))
        
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Fraction' and '{}'".format(type(other).__name__))
        

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == other.numerator * self.denominator
        else:
            raise TypeError("Unsupported operand type(s) for ==: 'Fraction' and '{}'".format(type(other).__name__))
        
       
    def __lt__(self, other):
         if isinstance(other, Fraction):
             return self.numerator * other.denominator < self.denominator * other.numerator
         else:
            raise TypeError("Unsupported operand type(s) for ==: 'Fraction' and '{}'".format(type(other).__name__))
        
   
    def __le__(self, other):
          if isinstance(other, Fraction):
               return self.numerator * other.denominator <= self.denominator * other.numerator    
          else:
            raise TypeError("Unsupported operand type(s) for ==: 'Fraction' and '{}'".format(type(other).__name__))
           
    
    def __gt__(self, other):
          if isinstance(other, Fraction):
             return self.numerator * other.denominator > self.denominator * other.numerator
          else:
            raise TypeError("Unsupported operand type(s) for ==: 'Fraction' and '{}'".format(type(other).__name__))
        
    def __ge__(self, other):
          if isinstance(other, Fraction):
                return self.numerator * other.denominator >= self.denominator * other.numerator
          else:
            raise TypeError("Unsupported operand type(s) for ==: 'Fraction' and '{}'".format(type(other).__name__))
        
    
    def __ne__(self, other):
          if isinstance(other, Fraction):
            return self.numerator * other.denominator != self.denominator * other.numerator
          else:
            raise TypeError("Unsupported operand type(s) for ==: 'Fraction' and '{}'".format(type(other).__name__))
        

    


f = Fraction(3, 4)
print(f)  # Output: 3/4

f1 = Fraction(5, 6)
print(f1)  # Output: 5/6

# operations
print(f + f1)  # Output: 38/24
print(f - f1)  # Output: -2/24
print(f * f1)  # Output: 15/24
print(f / f1)  # Output: 18/20
print(f == f1)  # Output: False
print(f < f1)  # Output: False
print(f <= f1)  # Output: False
print(f > f1)  # Output: True
print(f >= f1)  # Output: True
print(f != f1)  # Output: True

# print(dir(f))  # This will show all the attributes and methods of the f object


