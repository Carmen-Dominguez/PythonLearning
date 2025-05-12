
# Lists and Dictionaries Exercises

# 1. Favorite Movies
# This exercise creates a list of favorite movies and prints each movie on a new line.

# Define a list of favorite movies
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]

# Print each movie on a new line
print("favourite movies")
for movie in favorite_movies: 
    print(movie)

# 2. Shopping List
# This exercise creates a shopping list, adds and removes items, and prints the updated list.

# Create a shopping list
shopping_list = ["bread", "milk", "eggs"]

# Add items to the shopping list
shopping_list.append("butter")

# Remove an item from the shopping list
shopping_list.remove("milk")

# Print the updated shopping list
print("groceries")
for item in shopping_list:
    print(item)

# 3. Phone Book
# This exercise creates a dictionary to store names and phone numbers, then prints the dictionary.

# Create a phone book dictionary
phone_book = {
    "Bruce Wayne": "5553828378",
    "Damian Wayne": "5559287237",
    "Alfred Pennyworth": "5553923817"
}

# Add a new entry to the phone book
phone_book["Dick Grayson"] = "5552872728"

# Print the phone book
for name, number in phone_book.items():
    print(f"{name}: {number}")

# 4. Dictionary Modification
# This exercise modifies an existing dictionary by updating a key and adding a new one.

# Define a dictionary with name, age, and city
student_info = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}

# Modify the city
student_info["city"] = "New Haven"

# Add a new key-value pair for grade
student_info["grade"] = 98

# Print the updated dictionary
print(student_info)