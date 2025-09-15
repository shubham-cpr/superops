# --------------------------------------------
# LIST vs TUPLE vs DICTIONARY in Python
# --------------------------------------------

# ----------------------------
# Comparison Table
# ----------------------------

comparison_table = """
| Feature         | List ([])             | Tuple (())                 | Dictionary ({})                       |
|-----------------|-----------------------|----------------------------|---------------------------------------|
| Type            | Ordered collection    | Ordered collection         | Unordered key-value mapping           |
| Mutable?        | Yes                   | No                         | Yes                                   |
| Indexed?        | Yes (by position)     | Yes (by position)          | Yes (by key)                          |
| Duplicates?     | Allowed               | Allowed                    | Keys must be unique                   |
| Use Case        | Sequences (e.g. list) | Fixed records(e.g. coords) | Key-value mappings (e.g. configs)     |
| Syntax          | [1, 2, 3]             | (1, 2, 3)                  | {"name": "Alice"}                     |
| Can be nested?  | Yes                   | Yes                        | Yes                                   |
| Hashable?       | No                    | Yes (if items hashable)    | No  (keys must be hashable)           |
"""

print(comparison_table)

# ----------------------------
# 1. LIST (Mutable, Ordered)
# ----------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits[0])          # Access by index → 'apple'
fruits[1] = "mango"       # Mutable
print(fruits)             # ['apple', 'mango', 'cherry']

# ----------------------------
# 2. TUPLE (Immutable, Ordered)
# ----------------------------
colors = ("red", "green", "blue")
print(colors[1])          # Access by index → 'green'
# colors[0] = "yellow"    # Error: Tuples are immutable

# Single-element tuple
single = (5,)             # Tuple
not_tuple = (5)           # Just an int

# ----------------------------
# 3. DICTIONARY (Mutable, Key-Value)
# ----------------------------
person = {"name": "Alice", "age": 30}
print(person["name"])     # Access by key
person["age"] = 31        # Update
person["email"] = "a@example.com"

# ----------------------------
# 4. When to Use?
# ----------------------------
# List → When you need an ordered, mutable sequence (e.g., dynamic arrays, stacks, queues).
# Tuple → When your data should not change (e.g., coordinates, function returns, keys in dict).
# Dictionary → When you need fast lookups and key-value storage (e.g., user data, configs).