# Basic OOP Exercises

# 1. Dog Class
# This exercise creates a class for a dog with attributes and a method.
class Dog: 
    def __init__(self, name, weight, breed, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.breed = breed

    def bark(self):
        print(f"{self.name} goes bark!")

# Create instances of the Dog class
doggo = Dog("Bruno", 20, "Mutt", 40)
doggo.bark()

# 2. Rectangle Class
# This exercise creates a class for a rectangle and calculates its area and perimeter.
class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def calcArea(self):
        area =  1/2 * self.height * self.length
        return area
    
    def calcPerimeter(self):
        perimeter = 2 * (self.length + self.height)
        return perimeter

# Create an instance of the Rectangle class
rect = Rectangle(2, 5)

# Calculate and display area and perimeter
print(f"Area: {rect.calcArea()}")
print(f"Perimeter: {rect.calcPerimeter()}")


# 3. Bank Account Class
# This exercise creates a class for a bank account with deposit and withdraw methods.
class Bank:
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance

    def withdraw(self, amount):
        if (amount > self.balance):
            print("Cannot withdraw more than your balance, sorry.")
        else:
            print(f"Withdraw: {amount} from {self.balance}")
            self.balance = self.balance - amount
        return self.balance
        
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Depositing {amount}")
        return self.balance
    
    def currentBalance(self):
        print(f"Current Balance: {self.balance}")


# Create an instance of the BankAccount class
moMoney = Bank('Fo Shizzle', '36754378498', 2000)

# Perform deposit, withdrawal, and display balance
moMoney.withdraw(2200)
moMoney.deposit(500)
moMoney.withdraw(2200)

moMoney.currentBalance()

# 4. Book Class
# This exercise creates a class for a book with a description method.



# Create an instance of the Book class

# 5. Student Class
# This exercise creates a class for a student with a study method.


# Create an instance of the Student class

