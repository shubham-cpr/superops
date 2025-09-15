# Strings in Python are sequences of characters enclosed in single quotes, double quotes, or triple quotes. 
# They are immutable, meaning you can’t change them in place.

# ----------------------------
# 1. Creating Strings
# ----------------------------
a = 'hello'
b = "world"
c = '''multi-line
string'''
d = "I'm learning Python"

# ----------------------------
# 2. Accessing Characters
# ----------------------------
s = "Python"
print(s[0])    # 'P'
print(s[-1])   # 'n' (last character)

# ----------------------------
# 3. String Slicing
# ----------------------------
s = "abcdef"
print(s[1:4])   # 'bcd'
print(s[:3])    # 'abc'
print(s[3:])    # 'def'
print(s[::-1])  # 'fedcba' (reversed)

# ----------------------------
# 4. Common String Methods
# ----------------------------
s = " Hello, Python! "

print(s.lower())           # ' hello, python! '
print(s.upper())           # ' HELLO, PYTHON! '
print(s.strip())           # 'Hello, Python!' (removes surrounding spaces)
print(s.replace("Python", "World"))  # ' Hello, World! '
print(s.split(","))        # [' Hello', ' Python! ']
print(s.startswith(" "))   # True
print(s.endswith("! "))    # True
print(s.find("Python"))    # 8
print(s.count("o"))        # 2

# ----------------------------
# 5. String Concatenation and Repetition
# ----------------------------
a = "Hello"
b = "World"
print(a + " " + b)      # 'Hello World'
print(a * 3)            # 'HelloHelloHello'

# ----------------------------
# 6. String Formatting
# ----------------------------
name = "Alice"
age = 30

# f-string
print(f"My name is {name} and I am {age} years old")

# format()
print("My name is {} and I am {} years old".format(name, age))

# % formatting
print("My name is %s and I am %d years old" % (name, age))

# ----------------------------
# 7. Escape Characters
# ----------------------------
s = "She said \"Hello\""   # Double quote inside string
newline = "Line1\nLine2"   # New line
tabbed = "Col1\tCol2"      # Tab space

# ----------------------------
# 8. Multiline Strings
# ----------------------------
s = """This is
a multiline
string."""

# ----------------------------
# 9. Checking Membership
# ----------------------------
print("Py" in "Python")         # True
print("Java" not in "Python")   # True

# ----------------------------
# 10. str() Function – Type Casting
# ----------------------------

# Convert numbers, booleans to strings
num = 100
pi = 3.14
flag = True

str_num = str(num)     # '100'
str_pi = str(pi)       # '3.14'
str_flag = str(flag)   # 'True'

# Concatenate string with number (after casting)
name = "Alice"
age = 30
print("Name: " + name + ", Age: " + str(age))  # Output: Name: Alice, Age: 30