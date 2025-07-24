# What is a List?
"""
A list in Python is a collection that is ordered and mutable.
It is used to store multiple items in a single variable, similar to arrays in other languages.
"""

# Example:
age = [21, 22, 23, 20, 19, 18]
print("Access first element:", age[0])  # Output: 21

# Important Rules and Notes:
"""
1. Lists are defined using square brackets: []
2. Indexing starts from 0 (positive indexing) or -1 (negative indexing).
3. Lists are mutable: you can change, add, or remove elements.
4. Lists allow duplicate values.
5. Lists can hold items of different data types.
6. Lists can be nested (list inside another list).
"""

# List Methods 

fruits = ['apple', 'banana', 'cherry']
print("\nOriginal list:", fruits)

# 1. append() - Adds an element at the end
fruits.append('orange')
print("After append('orange'):", fruits)

# 2. insert(index, item) - Inserts item at specific position
fruits.insert(1, 'grape')
print("After insert(1, 'grape'):", fruits)

# 3. extend(list) - Adds elements from another iterable
fruits.extend(['kiwi', 'mango'])
print("After extend(['kiwi', 'mango']):", fruits)

# 4. remove(item) - Removes the first occurrence of item
fruits.remove('banana')
print("After remove('banana'):", fruits)

# 5. pop(index) - Removes and returns element at index (default last)
last_item = fruits.pop()
print("After pop():", fruits)
print("Popped item:", last_item)

# 6. clear() - Removes all elements
copy_fruits = fruits.copy()
copy_fruits.clear()
print("After clear():", copy_fruits)

# 7. index(item) - Returns first index of the item
print("Index of 'grape':", fruits.index('grape'))

# 8. count(item) - Returns count of item
print("Count of 'apple':", fruits.count('apple'))

# 9. sort() - Sorts list in place (ascending by default)
numbers = [5, 3, 9, 1, 4]
numbers.sort()
print("\nSorted numbers:", numbers)

# 10. reverse() - Reverses the list order
numbers.reverse()
print("Reversed numbers:", numbers)

# 11. copy() - Returns a shallow copy of the list
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)

# 12. len() - Returns number of elements
print("Length of fruits:", len(fruits))

# 13. in / not in - Membership check
print("'apple' in fruits:", 'apple' in fruits)
print("'banana' not in fruits:", 'banana' not in fruits)

# 14. del - Delete element by index or full list
del fruits[0]  # Deletes first element
print("After del fruits[0]:", fruits)

# 15. max(), min(), sum() - Useful with numerical lists
nums = [10, 20, 30, 40]
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

# Nested List (List inside List)
nested = [[1, 2], [3, 4], [5, 6]]
print("\nNested list:", nested)
print("Accessing nested item [1][0]:", nested[1][0])  # Output: 3
