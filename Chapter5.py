# In this file, all the dictionary and sets related code is going to be added

"""
What is a Dictionary?
- A dictionary in Python is an unordered collection of key-value pairs.
- Each key is unique and maps to a value.
- Syntax: my_dict = { key1: value1, key2: value2, ... }
"""

# Creating a dictionary
marks = {
    'Chris': 100,
    'Subham': 43,
    'Thor': 19
}

print("Original dictionary:", marks)
print("Type of marks:", type(marks))  # <class 'dict'>

# Accessing value using key
print("Marks of Chris:", marks['Chris'])

# Using .get() method (recommended, avoids error if key not found)
print("Marks of Thor using get:", marks.get('Thor'))
print("Try to access non-existing key using get():", marks.get('IronMan'))  # Returns None


# Adding a new key-value pair
marks['IronMan'] = 88
print("After adding IronMan:", marks)

# Updating existing value
marks['Thor'] = 50
print("After updating Thor's marks:", marks)


# Using del keyword
del marks['Subham']
print("After deleting Subham:", marks)

# Using pop() method
removed = marks.pop('IronMan')
print("Removed IronMan (pop):", removed)
print("Dictionary now:", marks)


student = {
    'name': 'Chris',
    'age': 21,
    'city': 'Jaipur'
}

# keys(), values(), items()
print("Keys:", student.keys())
print("Values:", student.values())
print("Items (key-value pairs):", student.items())

# update() - add or update multiple values
student.update({'email': 'chris@mail.com', 'age': 22})
print("After update():", student)

# clear() - remove everything
# student.clear()
# print("After clear():", student)


print("Is 'age' a key in student?", 'age' in student)
print("Is 'gender' not a key in student?", 'gender' not in student)



for key in student:
    print(key, "=>", student[key])

# Or using items()
for key, value in student.items():
    print(f"{key}: {value}")

# ------------------------ #
#     NESTED DICTIONARY
# ------------------------ #

nested = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}

print("Nested dictionary example:")
for person, info in nested.items():
    print(person)
    for key, value in info.items():
        print(f"  {key}: {value}")
