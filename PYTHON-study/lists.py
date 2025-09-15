# ----------------------------
# 1. Creating Lists
# ----------------------------
empty_list = []
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, [4, 5]]

# ----------------------------
# 2. Accessing Elements
# ----------------------------
print(fruits[0])     # 'apple'
print(fruits[-1])    # 'cherry' (last element)
print(mixed[3][1])   # 5 (nested list)

# ----------------------------
# 3. Slicing
# ----------------------------
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]
print(numbers[:3])     # [0, 1, 2]
print(numbers[3:])     # [3, 4, 5]
print(numbers[::-1])   # [5, 4, 3, 2, 1, 0]

# ----------------------------
# 4. List Length
# ----------------------------
print(len(fruits))     # 3

# ----------------------------
# 5. Modifying Lists
# ----------------------------
fruits[1] = "blueberry"    # Replace element
print(fruits)              # ['apple', 'blueberry', 'cherry']

# ----------------------------
# 6. Adding Elements
# ----------------------------
fruits.append("orange")          # Adds at end
fruits.insert(1, "kiwi")         # Insert at index
fruits.extend(["mango", "grape"])  # Add multiple elements
print(fruits)

# ----------------------------
# 7. Removing Elements
# ----------------------------
fruits.remove("kiwi")       # Removes first matching item
del fruits[0]               # Delete by index
last = fruits.pop()         # Removes and returns last item
print(fruits)
print("Popped:", last)

# ----------------------------
# 8. Searching & Counting
# ----------------------------
print("cherry" in fruits)         # True
print(fruits.index("cherry"))    # Index of value
print(fruits.count("mango"))     # Occurrences

# ----------------------------
# 9. Sorting and Reversing
# ----------------------------
nums = [3, 1, 4, 2]
nums.sort()              # Ascending sort
print(nums)
nums.sort(reverse=True)  # Descending sort
print(nums)
nums.reverse()           # Reverses list order
print(nums)

# ----------------------------
# 10. Copying Lists
# ----------------------------
original = [1, 2, 3]
copy1 = original.copy()          # Shallow copy
copy2 = list(original)           # Constructor
copy3 = original[:]              # Slice copy

# ----------------------------
# 11. Nested Lists
# ----------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix[1][2])  # 6

# ----------------------------
# 12. Looping Through Lists
# ----------------------------
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

# ----------------------------
# 13. List Comprehensions
# ----------------------------
squares = [x**2 for x in range(5)]            # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
nested = [[i for i in range(3)] for j in range(2)]  # [[0, 1, 2], [0, 1, 2]]

# ----------------------------
# 14. Other Useful Functions
# ----------------------------
print(min(nums))       # Smallest number
print(max(nums))       # Largest number
print(sum(nums))       # Sum of elements
print(sorted(nums))    # New sorted list (original not changed)

# ----------------------------
# 15. Clearing and Deleting
# ----------------------------
temp = [1, 2, 3]
temp.clear()        # Empties the list
del temp            # Deletes the variable completely

# 16. Adding (Concatenating) Lists
# ----------------------------
a = [1, 2, 3]
b = [4, 5, 6]
combined = a + b           # [1, 2, 3, 4, 5, 6]
print(combined)