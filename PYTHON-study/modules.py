# In Python, modules are files containing Python code — functions, classes, or variables. 
# You can import and reuse these in other Python scripts. 
# They help organize code, promote reuse, and maintain clarity in large projects.

# Types of Modules:
#   Built-in Modules – Already available with Python (e.g., math, random, os).
#   User-defined Modules – Python files you create (e.g., my_utils.py).
#   Third-party Modules – Installed using pip (e.g., numpy, requests).

# --------------------------------------------
# Modules in Python
# --------------------------------------------

# ----------------------------
# 1. Built-in Modules
# ----------------------------
import math
print(math.sqrt(16))       # 4.0
print(math.pi)             # 3.141592...

# Using alias
import math as m
print(m.pow(2, 3))         # 8.0

# Import specific functions
from math import sqrt, pi
print(sqrt(25), pi)

# Import everything (not recommended)
from math import *
print(cos(0))              # 1.0

# ----------------------------
# 2. Creating a Custom Module
# ----------------------------
# File: my_module.py
"""
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
"""

# File: main.py
"""
import my_module
print(my_module.greet("Shubham"))  # Hello, Shubham
print(my_module.PI)                # 3.14159
"""

# ----------------------------
# 3. __name__ == "__main__"
# ----------------------------
# File: my_module.py
"""
def greet():
    print("Hi!")

if __name__ == "__main__":
    print("This code runs only when executed directly.")
"""

# ----------------------------
# 4. Tools for Working with Modules
# ----------------------------
import random

print(dir(random))     # Lists all functions and attributes in random module
help(random.randint)   # Documentation for randint

# Reloading a module (useful during development)
from importlib import reload
reload(random)

# ----------------------------
# 5. Types of Modules
# ----------------------------
# Built-in: math, os, sys, time, random
# User-defined: your own .py files
# Third-party: install using pip → e.g., numpy, pandas, flask

# ----------------------------
# 6. Installing Third-Party Modules
# ----------------------------
# Run in terminal or notebook:
# pip install requests
"""
import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)
"""

# ----------------------------
# Summary
# ----------------------------
# Modules help organize and reuse code
# You can import full modules or parts
# Custom modules are just .py files
# Use __name__ guard for script vs import
