# ----------------------------
# 1. Defining a Basic Function
# ----------------------------
def greet():
    print("Hello, World!")

greet()  # Call the function

# ----------------------------
# 2. Function with Parameters
# ----------------------------
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# ----------------------------
# 3. Function with Return Value
# ----------------------------
def add(x, y):
    return x + y

result = add(3, 4)    # Call the function
print("Sum:", result)

# ----------------------------
# 4. Default Parameters
# ----------------------------
def greet_with_default(name="Guest"):
    print(f"Welcome, {name}!")

greet_with_default()         # Uses default
greet_with_default("Bob")    # Overrides default

# ----------------------------
# 5. Keyword Arguments
# ----------------------------
def order(item, quantity):
    print(f"{quantity} x {item}")

order(item="Burger", quantity=2)

# ----------------------------
# 6. Variable-Length Arguments: *args
# ----------------------------
def sum_all(*args):
    total = sum(args)
    print("Total:", total)

sum_all(1, 2, 3, 4)  # Args becomes a tuple

# ----------------------------
# 7. Variable-Length Keyword Arguments: **kwargs
# ----------------------------
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=30)

# ----------------------------
# 8. Multiple Return Values (Tuple)
# ----------------------------
def get_stats(numbers):
    return min(numbers), max(numbers)

low, high = get_stats([5, 2, 9])
print("Min:", low, "Max:", high)

# ----------------------------
# 9. Recursive Functions
# ----------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

# ----------------------------
# 10. Lambda (Anonymous) Functions
# ----------------------------
square = lambda x: x * x
print(square(6))  # 36

# With map:
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9]

# ----------------------------
# 11. Type Hints / Annotations (Optional)
# ----------------------------
def greet_with_type(name: str) -> None:
    print(f"Hello, {name}")

def add_with_type(a: int, b: int) -> int:
    return a + b

# ----------------------------
# 12. Scope: Local vs Global
# ----------------------------
global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(global_var)
    print(local_var)

scope_demo()
# print(local_var)  # Error: not defined outside

# ----------------------------
# 13. The 'global' Keyword
# ----------------------------
count = 0

def increment():
    global count
    count += 1

increment()
print("Count:", count)

# ----------------------------
# 14. Docstrings
# ----------------------------
def square_num(x):
    """Returns the square of a number."""
    return x * x

print(square_num.__doc__)

# ----------------------------
# 15. Pass Statement in Functions
# ----------------------------
def future_function():
    pass  # Placeholder for future logic

# ----------------------------
# 16. Common Mistakes
# ----------------------------

# Mistake 1: Forgetting parentheses when calling
# greet      # Won’t run the function, just references it

# Mistake 2: Returning None when return is omitted
def no_return():
    x = 5

print(no_return())  # Output: None

# Mistake 3: Mutable default arguments
def add_item(item, lst=[]):  # BAD PRACTICE
    lst.append(item)
    return lst

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana'] ← shared list

# Fix:
def add_item_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# ----------------------------
# 17. Positional vs Keyword (Named) Arguments
# ----------------------------

# Positional arguments are passed in order:
def describe_pet(animal, name):
    print(f"{name} is a {animal}")

describe_pet("dog", "Buddy")  # Positional: "dog" -> animal, "Buddy" -> name

# Keyword (named) arguments are passed with explicit parameter names:
describe_pet(name="Whiskers", animal="cat")  # Order doesn't matter with keywords

# Mixing positional and keyword:
describe_pet("rabbit", name="Fluffy")  # OK: positional first, then keyword

# Error: keyword before positional (not allowed)
# describe_pet(name="Goldie", "fish")  # SyntaxError

# ----------------------------
# Global vs Local Variables in for Loops
# ----------------------------
# In Python, variables declared in a for loop outside functions become global.
# But inside a function, they’re local to that function.

count = 0  # Global variable

def increment_all():
    # This 'i' is local to the function
    for i in range(5):
        print("Inside loop:", i)
    # 'i' is still accessible here because it's local to this function
    print("Final i inside function:", i)

increment_all()
# print(i)  # Error: 'i' is not defined outside the function

# Example modifying a global variable from inside a loop
total = 0

def add_to_total():
    global total
    for i in range(5):
        total += i
    print("Total inside function:", total)

add_to_total()
print("Total outside function:", total)

# Variable declared in a for loop (outside any function) is global
for j in range(3):
    pass

print("j after loop (global):", j)  # j is accessible globally if defined at module level
