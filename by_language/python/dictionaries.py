# Different ways to create dictionaries in Python

# 1. Using curly braces
person = {"name": "Alice", "age": 30, "city": "New York"}

# 2. Using the dict() constructor with keyword arguments
car = dict(make="Toyota", model="Camry", year=2020)

# 3. Using the dict() constructor with a list of tuples
grades = dict([("Alice", 95), ("Bob", 88), ("Charlie", 92)])

# 4. From two lists using zip()
keys = ["x", "y", "z"]
values = [10, 20, 30]
coordinates = dict(zip(keys, values))

# 5. Dictionary comprehension
squares = {x: x ** 2 for x in range(5)}

# ---------------------------
# Access and Modification
# ---------------------------

# Accessing values
name = person["name"]
age = person.get("age", "Unknown")  # get() avoids KeyError

# Adding or updating items
person["email"] = "alice@example.com"
person["age"] = 31  # update existing

# Removing items
del person["city"]
removed_value = person.pop("email", None)  # remove by key, with default

# Iterating over a dictionary
print("Iterating keys and values:")
for key, value in car.items():
    print(f"{key}: {value}")

# Iterating over keys only
print("Keys:", list(grades.keys()))

# Iterating over values only
print("Values:", list(grades.values()))

# Check if key exists
has_bob = "Bob" in grades

# Merge dictionaries (Python 3.9+)
merged = car | {"color": "blue"}  # New dict created

# Merge in-place (Python 3.9+)
car |= {"mileage": 50000}

# Merge (older versions, Python < 3.9)
combined = {**car, **{"owner": "Dan"}}

# Nested dictionaries
users = {
    "alice": {"age": 30, "email": "alice@example.com"},
    "bob": {"age": 25, "email": "bob@example.com"},
}

# Accessing nested dictionary
bob_email = users["bob"]["email"]

# ---------------------------
# Dictionary Utilities
# ---------------------------

# Dictionary length
num_users = len(users)

# Default value pattern with get()
user_city = person.get("city", "Unknown")

# Clear all items
temp = {"a": 1, "b": 2}
temp.clear()

# Create with default values (dict.fromkeys)
defaults = dict.fromkeys(["volume", "brightness", "contrast"], 50)

# ---------------------------
# Printing results (for demo)
# ---------------------------
if __name__ == "__main__":
    print("Person:", person)
    print("Car:", car)
    print("Grades:", grades)
    print("Coordinates:", coordinates)
    print("Squares:", squares)
    print("Merged dict:", merged)
    print("Users:", users)
    print("Bob's email:", bob_email)
    print("Default settings:", defaults)
