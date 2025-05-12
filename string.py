a = 'Chris';
b = "Hemsworth";
c = """I am Chris Hemsworth
I am murat also
"""

# print(a);
# print(b);
# print(c);

# print(len(b));

name = "Chris";
char1 = name[0];
print(char1);
print(name[-3:-1]);
nameShort = name[0:3];
print(nameShort);

print(name[:3]); # This is same as 0:3
print(name[0:]); # This is same as 0:length-1 This print the full string


# Skip Value

word = "Amazon";

print(word[1:4:2]);


# Inbuilt Function

words = "Harry Potter";
print(len(words));
print(words.endswith("rry"));
print(words.startswith("ha"));
print(words.capitalize()); #It only captilize the first letter of the first word.

print(words.find("H"));
