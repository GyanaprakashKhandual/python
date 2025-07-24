# Variables in python

a = 2;
b = 3;

print(a + b);

# Data types in python
"""
1. integers
2. strings
3. floating point number
4. booleans
5. nones
"""


# Integers data types
a = 1;

# Floating point number data types
b = 2.33;

# String data types;
c = "Chris";

# Boolean data type
d = False;

# None data types;
e = None;


# Rules for declaring variables in python
"""
1. Variable names must begin with a letter (a–z, A–Z) or an underscore (_), not a number.
2. Variable names can contain letters, digits (0–9), and underscores (_), but cannot contain special characters like @, $, or %.
3. Variable names are case-sensitive (e.g., 'name' and 'Name' are different variables).
"""


# Operator in Python

"""
1. Arithmetic Operators:
   +  Addition
   -  Subtraction
   *  Multiplication
   /  Division
   %  Modulus
   ** Exponentiation
   / Floor Division

2. Comparison (Relational) Operators:
   == Equal to
   != Not equal to
   >  Greater than
   <  Less than
   >= Greater than or equal to
   <= Less than or equal to

3. Assignment Operators:
   =   Assign
   +=  Add and assign
   -=  Subtract and assign
   *=  Multiply and assign
   /=  Divide and assign
   %=  Modulus and assign
   /= Floor divide and assign
   **= Exponentiate and assign
   &=  Bitwise AND and assign
   |=  Bitwise OR and assign
   ^=  Bitwise XOR and assign
   >>= Right shift and assign
   <<= Left shift and assign

4. Logical Operators:
   and  Logical AND
   or   Logical OR
   not  Logical NOT

5. Bitwise Operators:
   &  AND
   |  OR
   ^  XOR
   ~  NOT
   << Left shift
   >> Right shift

6. Membership Operators:
   in     Returns True if a value exists in a sequence
   not in Returns True if a value does not exist in a sequence

7. Identity Operators:
   is     Returns True if two variables point to the same object
   is not Returns True if two variables do not point to the same object
"""
# All Python Operators Demonstration

# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
print()

# 2. Comparison Operators
print("Comparison Operators:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)
print()

# 3. Assignment Operators
print("Assignment Operators:")
x = 5
x += 3; print("x += 3:", x)
x -= 2; print("x -= 2:", x)
x *= 2; print("x *= 2:", x)
x /= 2; print("x /= 2:", x)
x %= 3; print("x %= 3:", x)
x = 5
x //= 2; print("x //= 2:", x)
x **= 3; print("x **= 3:", x)
x &= 2; print("x &= 2:", x)
x |= 1; print("x |= 1:", x)
x ^= 3; print("x ^= 3:", x)
x <<= 1; print("x <<= 1:", x)
x >>= 2; print("x >>= 2:", x)
print()

# 4. Logical Operators
print("Logical Operators:")
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print()

# 5. Bitwise Operators
a = 5  # 0101
b = 3  # 0011
print("Bitwise Operators:")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT (~a):", ~a)
print("Left Shift a << 1:", a << 1)
print("Right Shift a >> 1:", a >> 1)
print()

# 6. Membership Operators
list_ = [1, 2, 3, 4]
print("Membership Operators:")
print("2 in list_:", 2 in list_)
print("5 not in list_:", 5 not in list_)
print()

# 7. Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("Identity Operators:")
print("x is y:", x is y)
print("x is z:", x is z)
print("x is not z:", x is not z)


# Type casting

a = 3;
a = type(a);
print(a);

b = 3.12;
c = type(b);
print(a);

# Variable changing via type casting

name = "31.2";
num = float(name);
oak = type(num);

print(oak);   # int, str and float are covert types one to another in python if the situation is valid


# Input and output in python

a = int(input("Enter number 1: "));
b = int(input("Enter number 2: "));

print("Number a is: ", a);
print("Number b is: ", b);
print("Sum is: ", a+b);


# To run the python code manually you have to run python your file name with .py in vs code terminal
