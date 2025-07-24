# String in Python declaration by simple printing

a = 'Chris'
b = "Chris"
c = """Chris"""
d = '''Chris'''

print(a, b, c, d)  # All valid string declarations in Python


# Indexing in String
"""
1. Indexing is used to access individual characters in a string.
2. Python strings are zero-indexed, meaning the first character is at index 0.
3. You can use both positive and negative indexing:
   - Positive indexing starts from 0 and goes forward.
   - Negative indexing starts from -1 (last character) and goes backward.
4. Syntax: string[index]

Example:
text = "Python"
text[0]    → 'P'   (first character)
text[2]    → 't'   (third character)
text[-1]   → 'n'   (last character)
text[-3]   → 'h'   (third character from end)

5. Trying to access an index out of range will raise an IndexError.
"""

name = "Murat"
nameShort = name[1:3]  # Slices from index 1 to 2 (3 is excluded)
print(nameShort)       # Output: 'ur'


# Slicing with skip value
word = 'Amazon'
print(word[0:3:1])     # Output: 'Ama', slice from 0 to 2 with step 1


# String Functions and Methods
name = 'Chris'

# Length of string
print(len(name))  # Output: 5

# Check if string ends with 's'
print(name.endswith('s'))  # Output: True

# Check if string starts with 'Ch'
print(name.startswith('Ch'))  # Output: True

# Convert to uppercase
print(name.upper())  # Output: 'CHRIS'

# Convert to lowercase
print(name.lower())  # Output: 'chris'

# Swap case (upper becomes lower and vice versa)
print(name.swapcase())  # Output: 'cHRIS'

# Capitalize first letter only
print(name.capitalize())  # Output: 'Chris'

# Replace a part of the string
print(name.replace('C', 'K'))  # Output: 'Khris'

# Find the position of a character
print(name.find('h'))  # Output: 2 (first occurrence)

# Count occurrences of a character
print(name.count('i'))  # Output: 1

# Check if all characters are alphabets
print(name.isalpha())  # Output: True

# Check if all characters are digits
print(name.isdigit())  # Output: False

# Check if string is in title case
print(name.istitle())  # Output: True

# Strip leading and trailing whitespace
msg = "  Hello  "
print(msg.strip())  # Output: 'Hello'

# Split the string into a list
data = "apple,banana,grape"
print(data.split(','))  # Output: ['apple', 'banana', 'grape']


# Problem 1: Write python programme for user credentials

name = input("Enter your name: ");

print(f"Good Afternoon {name}");

# Problem 2 : Use replace method in string and play a letter
letter = '''
Dear |<Name>|,
You are selected,
|<Date>|
'''

print(letter.replace('|<Name>|', 'Gyana prakash Khandual').replace('|<Date>|', 'June 24, 2025'));