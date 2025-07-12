# Different ways to create lists in Python

# 1. Using square brackets
fruits = ["apple", "banana", "cherry"]

# 2. Using the list() constructor
colors = list(("red", "green", "blue"))

# 3. From a string (split into characters)
letters = list("hello")

# 4. Using list comprehension
squares = [x ** 2 for x in range(10)]

# 5. Using range with list
numbers = list(range(10))

# 6. Repeating elements
zeros = [0] * 10

# 7. Nested lists (2D array)
matrix = [[1, 2], [3, 4], [5, 6]]

# 8. From other iterables (e.g., set, tuple, dict)
from_set = list({1, 2, 3})
from_tuple = list((4, 5, 6))
from_dict_keys = list({'a': 1, 'b': 2})
from_dict_values = list({'a': 1, 'b': 2}.values())

# ---------------------------
# Common List Operations
# ---------------------------

# Append item
fruits.append("date")

# Insert item at index
fruits.insert(1, "blueberry")

# Extend with another list
fruits.extend(["elderberry", "fig"])

# Remove item by value
fruits.remove("banana")

# Remove item by index
del fruits[0]

# Pop item (returns and removes last or indexed item)
last_item = fruits.pop()

# Index lookup
index_of_cherry = fruits.index("cherry") if "cherry" in fruits else -1

# Check membership
has_apple = "apple" in fruits

# Sort list (in-place)
numbers.sort(reverse=True)

# Reverse list (in-place)
numbers.reverse()

# Copy a list
copied = numbers.copy()

# Slice a list
first_three = numbers[:3]

# Iterate with index
for i, value in enumerate(fruits):
    print(f"{i}: {value}")

# Filter with comprehension
even_numbers = [n for n in numbers if n % 2 == 0]

# Map with comprehension
cubed_numbers = [n**3 for n in numbers]

# Flatten nested list
flat = [num for row in matrix for num in row]

# Zip lists together
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))

# Unpack zipped list
names_unzipped, scores_unzipped = zip(*combined)

# ---------------------------
# Printing results (for demo)
# ---------------------------
if __name__ == "__main__":
    print("Fruits:", fruits)
    print("Letters:", letters)
    print("Squares:", squares)
    print("Numbers:", numbers)
    print("Even numbers:", even_numbers)
    print("Cubed numbers:", cubed_numbers)
    print("Flattened matrix:", flat)
    print("Zipped names & scores:", combined)
