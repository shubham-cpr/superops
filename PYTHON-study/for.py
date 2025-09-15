# ----------------------------
# 1. Basic For Loop (Over a List)
# ----------------------------
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# ----------------------------
# 2. Using range() in Loops
# ----------------------------
for i in range(5):  # 0 to 4
    print(i)

for i in range(1, 6):  # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0 to 8 with step 2
    print(i)

# ----------------------------
# 3. Looping Through Strings
# ----------------------------
word = "Python"
for char in word:
    print(char)

# ----------------------------
# 4. Looping Through a Dictionary
# ----------------------------
person = {"name": "Alice", "age": 30}

for key in person:
    print(key, person[key])

# or

for key, value in person.items():
    print(f"{key} = {value}")

# ----------------------------
# 5. Looping with enumerate()
# ----------------------------
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)

# ----------------------------
# 6. Looping with zip()
# ----------------------------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# ----------------------------
# 7. Nested Loops
# ----------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# ----------------------------
# 8. Using break and continue
# ----------------------------
for num in range(1, 10):
    if num == 5:
        break   # Exit loop when num == 5
    print(num)

for num in range(1, 6):
    if num == 3:
        continue  # Skip number 3
    print(num)

# ----------------------------
# 9. Using else with for
# ----------------------------
# else runs only if the loop didn't break
for i in range(3):
    print(i)
else:
    print("Loop completed without break")

for i in range(3):
    if i == 1:
        break
else:
    print("You won't see this")

# ----------------------------
# 10. List Comprehensions (Compact Loops)
# ----------------------------
squares = [x**2 for x in range(5)]            # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]

# ----------------------------
# 11. For Loop Over Sets and Tuples
# ----------------------------
colors_set = {"red", "blue", "green"}
for color in colors_set:
    print(color)

values_tuple = (10, 20, 30)
for val in values_tuple:
    print(val)

# ----------------------------
# 12. Common Mistakes
# ----------------------------

# Mistake 1: Modifying list while iterating over it
nums = [1, 2, 3]
# for num in nums:
#     nums.remove(num)  # Dangerous!

# Correct way:
nums = [1, 2, 3]
for num in nums[:]:  # Iterate over a copy
    nums.remove(num)
print(nums)  # []

# Mistake 2: Forgetting colon
# for i in range(5)  # SyntaxError: expected ':'

# Mistake 3: Indentation errors
# for i in range(3):
# print(i)  # IndentationError

# ----------------------------
# 13. Looping Through Files (Advanced Example)
# ----------------------------
# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# ----------------------------
# 14. Using for with range(len(...))
# ----------------------------
items = ["a", "b", "c"]
for i in range(len(items)):
    print(f"Index {i} = {items[i]}")