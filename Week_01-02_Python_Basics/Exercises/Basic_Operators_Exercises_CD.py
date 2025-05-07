
# Basic Operators Exercises

# 1. Rectangle Area and Perimeter Calculation
# This exercise calculates the area and perimeter of a rectangle based on user-provided length and width.

# Get the length and width from the user
length = float(input('enter the length: '))
width = float(input('enetr the width: '))


# Calculate area (length * width)
area = length * width

# Calculate perimeter (2 * (length + width))
perimeter = 2 * (length + width)

# Display the results
print('area: ', area)
print('perimeter: ', perimeter)


# 2. Even or Odd Check
# This exercise checks if a given number is even or odd using the modulus operator.

# Get a number from the user
number = float(input('give number to check if even: '))


# Check if the number is even (remainder when divided by 2 is 0)
even = number % 2
print('is even: ', even == 0)

# 3. Power Calculation
# This exercise raises a base to a given exponent, which the user provides.

# Get base and exponent from the user
base = float(input('give base number: '))
exponent = float(input('give exponent: '))

# Calculate the power (base ** exponent)
power = base ** exponent

# Display the result
print(power)
