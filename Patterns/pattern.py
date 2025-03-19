# Pattern 1:
'''
def pattern1(n):
    for i in range(1, n+1):
        print("*"*i)

pattern1(5)
'''
'''
Output:
*
**
***
****
*****
'''

# Pattern 2:
'''
def pattern2(n):
    for i in range(n,0,-1):
        print("*"*i)

pattern2(5)'
'''
'''
Output:
*****
****
***
**
*
'''

# Pattern 3:
'''
def pattern3(n):
    for i in range(1, n+1):
           print(" "*(n-i) + "*"*(2*i-1))
           
pattern3(5)
'''
'''
Output:
    *
   ***
  *****
 *******
*********
'''

# Pattern 4:
'''
def pattern4(n):
    print("* "*n)
    for i in range(1, n+1-2):
        print("* " + "  "*(n-3) + " " + " *")
    print("* "*n)

pattern4(5)'
'''
'''
Output:
* * * * *
*       *
*       *
*       *
* * * * *
'''

# Pattern 5:
'''
def pattern5(n):
    for i in range(1, n+1):
       if i == 1:
           print(" "*(n-i) + "*")
       elif i == n:
           print("*"*(2*n-1))
       else:
           print(" "*(n-i) + "*" + " "*(2*i-3) + "*")

pattern5(5)
'''
'''
Output:
    *
   * *
  *   *
 *     *
*********
'''

# Pattern 6:
'''
def pattern6(n):
    for i in range(n, 0,-1):
        print(" "*(n-i) + "*"*(2*i-1))

pattern6(5)
'''
'''
Output:
*********
 *******
  *****
   ***
    *
'''

# Pattern 7:
'''
def pattern7(n):
    for i in range(n, 0, -1):
       if i == 1:
           print(" "*(n-i) + "*")
       elif i == n:
           print("*"*(2*n-1))
       else:
           print(" "*(n-i) + "*" + " "*(2*i-3) + "*")

pattern7(5)
'''
'''
Output:
*********
 *     *
  *   *
   * *
    *
'''

# Pattern 8:
'''
def draw_circle(radius):
    for y in range(-radius, radius + 1):  # Loop through y coordinates
        for x in range(-radius, radius + 1):  # Loop through x coordinates
            # Check if the point (x, y) is near the circle's equation
            if x**2 + y**2 <= radius**2 + radius:  # Approximation with a small error margin
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row of the circle

# Draw a circle with a radius of 10
draw_circle(5)
'''
'''
Output:
   *****   
  *******  
 ********* 
***********
***********
***********
***********
***********
 ********* 
  *******  
   *****
'''

# Pattern 9:
'''
def pattern9(n):
    for i in range(1, n+1):
        print("*"*i)
    
    for i in range(n, 0, -1):
        print("*"*i)

pattern9(5)
'''
'''
Output:
*
**
***
****
*****
*****
****
***
**
*
'''

# Pattern 10:
'''
def pattern10(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))

    for i in range(n-1, 0, -1):
        print(" "*(n-i) + "*"*(2*i-1))

pattern10(5)
'''
'''
Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''




