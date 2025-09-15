# ----------------------------
# 1. Creating a Tuple
# ----------------------------
t = (1, 2, 3)
empty = ()              # Empty tuple
single = (5,)           # Single-element tuple needs comma

# ----------------------------
# 2. Accessing Elements
# ----------------------------
print(t[0])   # 1
print(t[-1])  # 3

# ----------------------------
# 3. Tuple is Immutable
# ----------------------------
# t[1] = 10  # TypeError

# ----------------------------
# 4. Tuple Methods
# ----------------------------
print(t.count(2))  # 1
print(t.index(3))  # 2

# ----------------------------
# 5. Looping Through Tuples
# ----------------------------
for item in t:
    print(item)

# ----------------------------
# 6. Tuple Unpacking
# ----------------------------
a, b, c = t
print(a, b, c)

# ----------------------------
# 7. Swapping Values
# ----------------------------
x, y = 10, 20
x, y = y, x  # Swap using tuple unpacking

# ----------------------------
# 8. Tuples with Different Data Types
# ----------------------------
mixed = (1, "apple", True)

# ----------------------------
# 9. Nesting Tuples
# ----------------------------
nested = ((1, 2), (3, 4))
print(nested[1][0])  # 3

# ----------------------------
# 10. Tuple as Dictionary Keys
# ----------------------------
locations = {
    (27.7, 85.3): "Kathmandu",
    (51.5, -0.1): "London"
}
print(locations[(27.7, 85.3)])

# ----------------------------
# 11. Converting List ↔ Tuple
# ----------------------------
l = [1, 2, 3]
t = tuple(l)
l2 = list(t)

# ----------------------------
# 12. Common Mistakes
# ----------------------------

# Forgetting comma in single-item tuple
single = ("item")    # ❌ Not a tuple, it's a string
correct = ("item",)  # ✅

# Trying to modify a tuple
# t[0] = 100  # TypeError

# Unpacking mismatch
# a, b = (1, 2, 3)  # ❌ ValueError
