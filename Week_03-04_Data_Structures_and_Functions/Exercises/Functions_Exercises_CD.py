
# Functions Exercises

# 1. Simple Greeting Function
# This exercise creates a function that takes a name as input and prints a greeting message.
def greeting(name):
    print(f"Hello {name}")


# Call the function with example names
greeting("John")

# 2. Addition Function
# This exercise creates a function that takes two numbers as input, adds them, and returns the result.
def addition(num1, num2):
    return num1 + num2

# Call the function and display the result
print(addition(2, 3))

# 3. Rectangle Area
# This exercise creates a function that calculates the area of a rectangle given its length and width.
def rectArea(length, width):
    return length * width

# Call the function with example dimensions
print(rectArea(2, 3))

# 4. Temperature Converter
# This exercise creates a function to convert Celsius to Fahrenheit.
# celsius * 9 / 5 + 32
def tempConvert(temp):
    return temp * 9 / 5 + 32

# Call the function with an example temperature
convert = tempConvert(25)
print(f"From Celcius to Farheneit: {convert}")

# 5. Factorial Function
# This exercise creates a function that calculates the factorial of a given number.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Call the function with an example number
print(factorial(10))

# 6. Shopping Cart Total
# This exercise calculates the total cost of items in a shopping cart.
cart = {"bread": 10, "milk": 12, "eggs": 20}

def calcTotal(cart):
    total = 0
    for item, price in cart.items():
        total = total + price
    return total

print(calcTotal(cart))

# Example shopping cart prices
