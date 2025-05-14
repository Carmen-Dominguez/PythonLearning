# File Handling Exercises

# 1. Write and Read a File
# This exercise creates a file, writes multiple lines to it, and reads its content.

# Writing to a file
with open("notes.txt", "w") as file:
    file.write('I am inevatible!\n')
    file.write('And I ...\n')
    file.write('Am Ironman.\n') 

# Reading from the file
print("Content of 'notes.txt':")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# 2. Append Data to an Existing File
# This exercise appends data to an existing file and displays the updated content.
# Appending to the file
with open('notes.txt', 'a') as file:
    file.write("December 16, 1991\n")

# Reading the updated file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)


# 3. Count Words in a File
# This exercise counts the number of words in a file.

# Reading the file and counting words
with open("notes.txt", "r") as file:
    for line in file:
        content = content + line.strip()
    words = content.split(' ')

    print(f"The file 'notes.txt' contains {len(words)} words.")

# 4. Copy File Content
# This exercise copies the content of one file to another.
with open("notes.txt", "r") as file:
    content = file.read()

with open("copy.txt", "w") as file:
    file.write(content)

print("Content copied to 'copy.txt'.")
print(content)

# 5. Search for a Word in a File
# This exercise searches for a specific word in a file and counts its occurrences.
search_word = "Ironman"
with open("notes.txt", "r") as file:
    content = file.read()

# Searching for the word in the file
    if (content.find(search_word) > -1):
        print(f"Found {search_word}")
    else:
        print(f"Did not find {search_word}")


# 6. Create a Log File
# This exercise appends a timestamped log message to a log file.
import datetime

# Appending a log entry with a timestamp
with open("copy.txt", "a") as file:
    file.write(f"{datetime.datetime.now()}: Log entry added\n")

print("Log entry added to 'copy.txt'.")
with open("copy.txt", "r") as file:
    content = file.read()
    print(content)

# 7. Handle File Not Found Error
# This exercise demonstrates handling errors when a file is not found.
try:
    with open("noExist.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'noExist.txt' was not found.")


# 8. Read File Line by Line
# This exercise reads a file line by line and prints each line.
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# 9. Write a Function for File Handling
# This exercise creates a function that writes and reads from a file.
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()
