# numbers are a built-in data type used to represent numeric values. 
# They are immutable, and Python handles them automatically based on their value.

# ----------------------------
# 1. Types of Numbers
# ----------------------------

# Integer (int)
a = 10
b = -200
c = 9999999999999999  # Python supports large integers

# Floating-point (float)
x = 3.14
y = -0.0001
z = 1.0

# Complex numbers (complex)
c1 = 3 + 4j
print("Real part:", c1.real)  # 3.0
print("Imaginary part:", c1.imag)  # 4.0

# ----------------------------
# 2. Type Conversion
# ----------------------------
print(int(5.9))       # 5
print(float(10))      # 10.0
print(complex(3))     # (3+0j)

# ----------------------------
# 3. Arithmetic Operators
# ----------------------------
a = 9
b = 4

print(a + b)     # 13 (Addition)
print(a - b)     # 5 (Subtraction)
print(a * b)     # 36 (Multiplication)
print(a / b)     # 2.25 (True division)
print(a // b)    # 2 (Floor division)
print(a % b)     # 1 (Modulus)
print(a ** b)    # 6561 (Exponentiation)

# ------------------------