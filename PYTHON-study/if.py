number=input("Enter your number: ")
number=int(number)
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")

#### OR ####

number=int(input("Enter your number: "))
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")

# ----------------------------
# 1. Basic If Statement
# ----------------------------
x = 10
if x > 5:
    print("x is greater than 5")  # Indentation is mandatory

# ----------------------------
# 2. If-Else Statement
# ----------------------------
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ----------------------------
# 3. If-Elif-Else Chain
# ----------------------------
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Fail")

# ----------------------------
# 4. Logical Operators (and, or, not)
# ----------------------------
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or not has_license:
    print("Cannot drive")

# ----------------------------
# 5. Nested If Statements
# ----------------------------
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("No license")
else:
    print("Too young to drive")

# ----------------------------
# 6. One-liner If Statements (Ternary Operator)
# ----------------------------
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Outputs: Odd

# ----------------------------
# 7. Comparing Values (==, !=, <, >, <=, >=)
# ----------------------------
a = 5
b = 10

if a != b:
    print("a and b are not equal")
if a <= b:
    print("a is less than or equal to b")

# ----------------------------
# 8. Checking Identity (is / is not)
# ----------------------------
a = [1, 2]
b = a
c = [1, 2]

print(a == c)      # True: values are equal
print(a is c)      # False: different memory locations
print(a is b)      # True: same object

# ----------------------------
# 9. Checking Membership (in / not in)
# ----------------------------
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")

# ----------------------------
# 10. Truthy and Falsy Values
# ----------------------------
# Falsy values: False, None, 0, 0.0, "", [], {}, set(), range(0)

if "":
    print("This won't print")

if "Hello":
    print("This will print")  # Non-empty string is truthy

# ----------------------------
# 11. Pass Statement (Placeholder)
# ----------------------------
x = 10
if x > 5:
    pass  # Do nothing for now (avoids syntax error)

# ----------------------------
# 12. Using Boolean Variables
# ----------------------------
is_active = True

if is_active:
    print("Active")
else:
    print("Inactive")

# ----------------------------
# 13. Combining Conditions for Clarity
# ----------------------------
# Instead of deeply nested conditions:
if age >= 18 and has_license:
    print("Can drive")
# Avoids unnecessary nesting

# ----------------------------
# 14. Using match-case (Python 3.10+ alternative to if-elif)
# ----------------------------
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")

# ----------------------------
# 15. Common Mistakes
# ----------------------------

# Mistake 1: Using '=' instead of '=='
# if x = 5:   # SyntaxError

# Mistake 2: Missing indentation
# if True:
# print("Hi")  # IndentationError

# Mistake 3: Dangling else without if
# else: print("No if above")  # SyntaxError