Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("hello world")
hello world
x=10
y=20
print(x+y)
30
# Program to check if a number is even or odd

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
Enter a number: 7
7 is Odd
Enter a number: 12
12 is Even
# Program to check leap year and even/odd

# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
Enter a year: 2024
2024 is a Leap Year
Enter a number: 15
15 is Odd
Enter a year: 1900
1900 is Not a Leap Year
Enter a number: 42
42 is Even
import math

# Print the value of pi
print("The value of pi is:", math.pi)
The value of pi is: 3.141592653589793
# Store a constant value
PI = 3.14159
GRAVITY = 9.8

# Print the constant values
print("The value of PI is:", PI)
print("The value of GRAVITY is:", GRAVITY)
The value of PI is: 3.14159
The value of GRAVITY is: 9.8
# Program to find the square of a number

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Calculate the square
square = num ** 2   # or num * num

# Print the result
print(f"The square of {num} is {square}")
Enter a number: 5
The square of 5 is 25
import math

# Program to calculate area of a circle

# Ask the user to enter the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area using formula: πr²
area = math.pi * radius ** 2

# Print the result
print(f"The area of the circle with radius {radius} is {area:.2f}")
Enter the radius of the circle: 7
The area of the circle with radius 7.0 is 153.94
# Program to check data type

# Example values
a = 10
b = 3.14
c = "Hello"
d = True

# Print their data types
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))
Type of a: <class 'int'>
Type of b: <class 'float'>
Type of c: <class 'str'>
Type of d: <class 'bool'>
import math

# Common math functions

# Square root
print("Square root of 16:", math.sqrt(16))

# Power
print("2 raised to 3:", math.pow(2, 3))

# Trigonometric functions (angles in radians)
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Cosine of 0 degrees:", math.cos(math.radians(0)))

# Logarithms
print("Natural log of 10:", math.log(10))
print("Log base 10 of 1000:", math.log10(1000))

# Rounding functions
print("Floor of 3.7:", math.floor(3.7))
print("Ceiling of 3.7:", math.ceil(3.7))

# Constants
print("Pi value:", math.pi)
print("Euler's number (e):", math.e)
Square root of 16: 4.0
2 raised to 3: 8.0
Sine of 90 degrees: 1.0
Cosine of 0 degrees: 1.0
Natural log of 10: 2.302585092994046
Log base 10 of 1000: 3.0
Floor of 3.7: 3
Ceiling of 3.7: 4
Pi value: 3.141592653589793
Euler's number (e): 2.718281828459045
# Program to find power of a number

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = base ** exponent
print(f"{base} raised to {exponent} is {result}")
Enter the base number: 2
Enter the exponent: 5
2 raised to 5 is 32
# Program to check if a number is positive, negative, or zero

# Ask the user to enter a number
num = float(input("Enter a number: "))

# Check the number
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("The number is Zero")
Enter a number: 12
12.0 is Positive
Enter a number: -5
-5.0 is Negative
Enter a number: 0
The number is Zero
