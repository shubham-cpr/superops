# ----------------------------
# 1. Creating Variables
# ----------------------------
x = 5               # Integer
name = "Alice"      # String
pi = 3.14           # Float

# ----------------------------
# 2. Variable Naming Rules
# ----------------------------
valid_name = 10     # Valid
_name2 = "hello"    # Valid
# 2name = 10        # Invalid: starts with number
# name$ = "test"    # Invalid: special character
# if = 5            # Invalid: Python keyword

# ----------------------------
# 3. Variable Types
# ----------------------------
a = 10              # int
b = 3.14            # float
c = "hello"         # str
d = True            # bool
e = [1, 2, 3]       # list
f = (1, 2, 3)       # tuple
g = {"a": 1}        # dict
h = None            # NoneType

# ----------------------------
# 4. Multiple Assignments
# ----------------------------
x, y, z = 1, 2, 3   # Multiple variables at once
a = b = c = "same"  # Same value to multiple variables

# ----------------------------
# 5. Variable Scope
# ----------------------------
x = 10  # Global variable

def my_func():
    x = 5  # Local variable
    print("Inside function:", x)

my_func()            # Output: 5
print("Outside function:", x)  # Output: 10

# Using 'global' keyword
def modify_global():
    global x
    x = 20

modify_global()
print("After global modification:", x)  # Output: 20

# ----------------------------
# 6. Constants (By Convention)
# ----------------------------
PI = 3.14159
MAX_USERS = 100
# Note: Constants are not enforced in Python

# ----------------------------
# 7. Type Casting
# ----------------------------
# Casting (or type conversion) in Python refers to converting a variable from one data type to another. Python supports explicit and implicit casting.

num = int("5")       # str to int
decimal = float("3.14")  # str to float
text = str(10)       # int to str

# String to int
a = int("5")          # 5 (int)

# Float to int (truncates decimal)
b = int(3.99)         # 3

# Int to float
c = float(7)          # 7.0

# Number to string
d = str(123)          # "123"

# Boolean to int
e = int(True)         # 1
f = int(False)        # 0

# Int to bool
g = bool(0)           # False
h = bool(5)           # True

# Note: Invalid conversions raise errors.
int("abc")    # ValueError
float("xyz")  # ValueError

# Tuple to list
a = list((1, 2, 3))       # [1, 2, 3]

# List to set (removes duplicates)
b = set([1, 2, 2, 3])     # {1, 2, 3}

# List of tuples to dict
c = dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}

# String to list
d = list("hello")         # ['h', 'e', 'l', 'l', 'o']

# ----------------------------
# 8. Deleting Variables
# ----------------------------
temp = 100
del temp  # Deletes the variable from memory
# print(temp)  # Will cause NameError