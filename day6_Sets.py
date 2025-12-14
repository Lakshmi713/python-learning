# Creating Sets
numbers = {10, 20, 30, 40}
fruits = {"apple", "banana", "mango"}
print("Numbers Set:", numbers)
print("Fruits Set:", fruits)

# Sets remove duplicates automatically
numbers = {10, 20, 20, 30, 10}
print("Unique Numbers:", numbers)

# Adding Elements
fruits = {"apple", "banana"}
fruits.add("mango")
print("After adding mango:", fruits)

# Removing Elements
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")   # error if element not present
fruits.discard("grape")   # no error if not present
print("After removing:", fruits)

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference a-b:", a - b)
print("Difference b-a:", b - a)
print("Symmetric Difference:", a ^ b)

# Check Membership
fruits = {"apple", "banana", "mango"}
print("Is apple in fruits?", "apple" in fruits)
print("Is grape in fruits?", "grape" in fruits)
