# Condition in Python programming

# Simple if-else: Check even or odd
a = int(input('Enter a number: '))
if a % 2 == 0:
    print('You entered an even number')
else:
    print('You entered an odd number')



# Ladder if-elif-else condition: Age check

# This is called a ladder condition (or chained condition)
a = int(input('Enter your age: '))

if a >= 18:
    print('You are eligible to marry')
elif a < 0:
    print('You are entering a negative number')
elif a == 0:
    print('Age cannot be zero')
else:
    print('You are not eligible to marry')


# Multi if condition example

# In this case, all 'if' blocks will be checked independently

print('\n--- Health Check Report ---')
temperature = float(input('Enter your body temperature in °C: '))
bp = int(input('Enter your blood pressure (systolic): '))
sugar = int(input('Enter your fasting blood sugar level (mg/dL): '))

if temperature > 37.5:
    print('You have a fever')

if bp > 130:
    print('High blood pressure detected')

if sugar > 110:
    print('High blood sugar level detected')

if temperature <= 37.5 and bp <= 130 and sugar <= 110:
    print('All your vitals are normal')

# Note: Unlike if-elif-else, multiple if statements all run independently


# Problem - 1 : Find the greatest number from 4 number using input in python?

a1 = int(input('Enter number 1: '));
a2 = int(input('Enter number 2: '));
a3 = int(input('Enter number 3: '));
a4 = int(input('Enter number 4: '));


if( a1>a2 and a1>a3 and a1>a4): 
    print('a1 is the greatest number: ', a1);
elif( a2>a1 and a2>a3 and a2>a4):
    print('a2 is the greatest number: ', a2);
elif( a3>a1 and a3>a2 and a3>a4):
    print('a3 is the greatest number: ', a3);
elif( a4>a1 and a4>a2 and a4>a3): 
    print('a4 is the greatest number: ', a4);



# Problem - 2 : Find the user is passed or not?

marks1 = int(input('Enter marks: 1: '));
marks2 = int(input('Enter marks: 2: '));
marks3 = int(input('Enter marks: 3: '));

# Check for total percentage

total_percentage = (100*marks1 + marks2 + marks3)/300;
if(marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and total_percentage >= 40) :
    print('Congratulation You are passed');
    print(total_percentage)
else:
    print('Better luck next time');
    print(total_percentage)


# Problem - 3 : Find the spam comments

# -----------------------------
# Spam Detection Program
# -----------------------------

# Common spammy phrases
comment1 = "make a lot of money"
comment2 = "buy now"
comment3 = "subscribe this"
comment4 = "click this"

# Take user input
message = input('Enter your comment: ').lower()  # Convert to lowercase for case-insensitive matching

# Check for spam using multi-condition OR
if (comment1 in message or comment2 in message or comment3 in message or comment4 in message):
    print("This comment is detected as spam!")
else:
    print("This comment looks clean.");



