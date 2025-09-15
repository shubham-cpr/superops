# ----------------------------
# 1. Creating a Dictionary
# ----------------------------
person = {"name": "Alice", "age": 30, "city": "New York"}

# ----------------------------
# 2. Accessing Values
# ----------------------------
print(person["name"])        # Alice
print(person.get("age"))     # 30
print(person.get("gender"))  # None (safe access)

# ----------------------------
# 3. Adding / Updating Values
# ----------------------------
person["email"] = "alice@example.com"
person["age"] = 31

# ----------------------------
# 4. Removing Items
# ----------------------------
del person["city"]
person.pop("email")
person.popitem()  # Removes last inserted item (Python 3.7+)

# ----------------------------
# 5. Dictionary Methods
# ----------------------------
print(person.keys())       # dict_keys(['name', 'age'])
print(person.values())     # dict_values(['Alice', 31])
print(person.items())      # dict_items([('name', 'Alice'), ('age', 31)])

# ----------------------------
# 6. Looping Through Dictionary
# ----------------------------
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# ----------------------------
# 7. Checking Keys
# ----------------------------
if "name" in person:
    print("Key exists")

# ----------------------------
# 8. Dictionary Comprehension
# ----------------------------
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, ..., 4: 16}

# ----------------------------
# 9. Nested Dictionary
# ----------------------------
students = {
    "101": {"name": "Alice", "grade": "A"},
    "102": {"name": "Bob", "grade": "B"},
}

print(students["101"]["name"])

# ----------------------------
# 10. Copying Dictionaries
# ----------------------------
copy1 = person.copy()        # Shallow copy
copy2 = dict(person)         # Another way

# ----------------------------
# 11. Clearing Dictionary
# ----------------------------
person.clear()

# ----------------------------
# 12. Common Mistakes
# ----------------------------

# Accessing missing key without get()
# print(person["gender"])  # KeyError

# Using mutable types as keys
# d = {[1, 2]: "value"}  # TypeError: list is unhashable

# Correct: Use immutable types like tuple
d = {(1, 2): "value"}