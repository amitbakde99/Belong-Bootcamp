#1.Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. Input “fname” as your first name and “lname” as your last name. Test it for Harry Potter.

fname=input()
lname=input()
print(lname+fname)

#2.Write a Python program that calculates the area of a circle based on the radius entered by the user. Input “r” as the radius of the circle that can accept float values also. Define the value of pi as 3.14.

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)

#3.Write a Python program to calculate the sum of three given numbers. Take the 3 inputs from the user and print the result.

sum_of_numbers = sum(float(input()) for _ in range(3))
print(sum_of_numbers)

#4.Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints either Even or Odd after testing the number.

num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

#5.Write a Python program that accepts an integer (n) and computes the value of (n+n*n+n*n*n

n = int(input("Enter an integer: "))
result = n + n * n + n * n * n
print("Result:", result)

#6.Write a Python program to solve (x + y) * (x + y)
-->
x = 5
y = 3
result = (x + y) ** 2
print(result)

#7.Write a python program to print greater of the two input numbers. Input a and b as two numbers. If a is greater than b then print “a is greater”. If b is greater than a print “b is greater”

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("Both numbers are equal")

#8.Write a python code to perform the following operations on two input numbers ( a and b) on a new lines. Sum, Subtraction, Multiplication, Division, Modulo, Power

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Sum
sum_result = a + b
print("Sum:", sum_result)

# Subtraction
subtraction_result = a - b
print("Subtraction:", subtraction_result)

# Multiplication
multiplication_result = a * b
print("Multiplication:", multiplication_result)

# Division
if b != 0:
    division_result = a / b
    print("Division:", division_result)
else:
    print("Division: Cannot divide by zero")

# Modulo
if b != 0:
    modulo_result = a % b
    print("Modulo:", modulo_result)
else:
    print("Modulo: Cannot perform modulo with zero")

# Power
power_result = a ** b
print("Power:", power_result)
