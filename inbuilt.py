# 1. capitalize()
print("hello world".capitalize())  # Hello world

# 2. casefold()
print("HELLO".casefold())  # hello

# 3. center()
print("python".center(10, '-'))  # --python--

# 4. count()
print("banana".count("a"))  # 3

# 5. encode()
print("hello".encode())  # b'hello'

# 6. endswith()
print("hello.py".endswith(".py"))  # True

# 7. expandtabs()
print("a\tb".expandtabs(4))  # a   b

# 8. find()
print("hello world".find("world"))  # 6

# 9. format()
print("My name is {}".format("Chris"))  # My name is Chris

# 10. format_map()
print("{x} + {y}".format_map({'x': 1, 'y': 2}))  # 1 + 2

# 11. index()
print("hello".index("e"))  # 1

# 12. isalnum()
print("abc123".isalnum())  # True

# 13. isalpha()
print("abc".isalpha())  # True

# 14. isascii()
print("abc".isascii())  # True

# 15. isdecimal()
print("123".isdecimal())  # True

# 16. isdigit()
print("123".isdigit())  # True

# 17. isidentifier()
print("variable".isidentifier())  # True

# 18. islower()
print("hello".islower())  # True

# 19. isnumeric()
print("123".isnumeric())  # True

# 20. isprintable()
print("hello\n".isprintable())  # False

# 21. isspace()
print("   ".isspace())  # True

# 22. istitle()
print("Hello World".istitle())  # True

# 23. isupper()
print("HELLO".isupper())  # True

# 24. join()
print("-".join(["a", "b", "c"]))  # a-b-c

# 25. ljust()
print("cat".ljust(5, "."))  # cat..

# 26. lower()
print("PYTHON".lower())  # python

# 27. lstrip()
print("  hello".lstrip())  # 'hello'

# 28. maketrans() + translate()
trans = str.maketrans("ae", "12")
print("apple".translate(trans))  # 1ppl2

# 29. partition()
print("email@example.com".partition("@"))  # ('email', '@', 'example.com')

# 30. removeprefix()
print("unhappy".removeprefix("un"))  # happy

# 31. removesuffix()
print("test.py".removesuffix(".py"))  # test

# 32. replace()
print("hello world".replace("world", "Python"))  # hello Python

# 33. rfind()
print("hello world".rfind("o"))  # 7

# 34. rindex()
print("hello".rindex("l"))  # 3

# 35. rjust()
print("cat".rjust(5, "."))  # ..cat

# 36. rsplit()
print("a,b,c".rsplit(",", 1))  # ['a,b', 'c']

# 37. rstrip()
print("hello  ".rstrip())  # 'hello'

# 38. split()
print("a b c".split())  # ['a', 'b', 'c']

# 39. splitlines()
print("line1\nline2".splitlines())  # ['line1', 'line2']

# 40. startswith()
print("hello.py".startswith("hello"))  # True

# 41. strip()
print("  hello  ".strip())  # 'hello'

# 42. swapcase()
print("HeLLo".swapcase())  # hEllO

# 43. title()
print("hello world".title())  # Hello World

# 44. upper()
print("python".upper())  # PYTHON

# 45. zfill()
print("42".zfill(5))  # 00042
