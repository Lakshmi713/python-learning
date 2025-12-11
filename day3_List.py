# 1. Create a List
fruits = ["apple", "banana", "mango"]
print("Fruits:", fruits)

# 2. Accessing List Items
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# 3. Add Items to List
fruits.append("orange")
print("After adding:", fruits)

# 4. Insert at a Specific Position
numbers = [10, 20, 40]
numbers.insert(2, 30)
print("After insert:", numbers)

# 5. Remove Item
fruits.remove("banana")
print("After removing banana:", fruits)

# 6. List Length
names = ["Lakshmi", "Ram", "Sita"]
print("Total names:", len(names))

# 7. Loop Through List
colors = ["red", "blue", "green"]
for c in colors:
    print("Color:", c)

# 8. List Slicing
nums = [10, 20, 30, 40, 50]
print("First 3 numbers:", nums[:3])

# 9. Sort a List
numbers2 = [5, 2, 9, 1]
numbers2.sort()
print("Sorted list:", numbers2)

# 10. Mixed Data List
details = ["Lakshmi", 20, 5.6, True]
print("Details:", details)
