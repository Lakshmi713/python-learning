# 1. Create a Dictionary
student = {
    "name": "Lakshmi",
    "age": 18,
    "city": "Nuzvid"
}
print("Student:", student)

# 2. Access Dictionary Values
print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"])

# 3. Add New Key-Value Pair
student["course"] = "CSE"
print("After adding course:", student)

# 4. Update Existing Value
student["age"] = 21
print("After updating age:", student)

# 5. Remove a Key-Value Pair
student.pop("city")
print("After removing city:", student)

# 6. Dictionary Length
print("Total items:", len(student))

# 7. Loop Through Dictionary Keys
print("Keys:")
for key in student:
    print(key)

# 8. Loop Through Dictionary Values
print("Values:")
for value in student.values():
    print(value)

# 9. Loop Through Both Keys and Values
print("Key-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# 10. Nested Dictionary
college = {
    "student1": {"name": "Lakshmi", "age": 18},
    "student2": {"name": "Ram", "age": 22}
}
print("College:", college)
