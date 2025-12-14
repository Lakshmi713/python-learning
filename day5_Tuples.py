# 1. Tuple Variable – multiple values (immutable)
fruits = ("apple", "banana", "mango")
numbers = (10, 20, 30, 40)
mixed = ("hello", 50, True)

print("Fruits Tuple:", fruits)
print("Numbers Tuple:", numbers)
print("Mixed Tuple:", mixed)

# 2. Accessing tuple elements
print("First Fruit:", fruits[0])
print("Last Number:", numbers[-1])

# 3. Slicing tuple
print("First two fruits:", fruits[0:2])

# 4. Tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Combined Tuple:", combined)
print("Repeated Tuple:", tuple1 * 2)

# 5. Check element in tuple
print("Is 'banana' in fruits?", "banana" in fruits)
print("Is 100 in numbers?", 100 in numbers)
