# 1. Creating Strings
name = "Lakshmi"
college = "RGUKT"
print("Name:", name)
print("College:", college)

# 2. Accessing Characters
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])

# 3. String Slicing
text = "Programming"
print("First 5 characters:", text[0:5])
print("From index 3:", text[3:])
print("Middle part:", text[3:8])

# 4. String Length
print("Length:", len(text))

# 5. Changing Case
sentence = "Python Programming"
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Capitalize:", sentence.capitalize())
print("Swap case:", sentence.swapcase())

# 6. Removing Spaces
msg = "  Hello World  "
print("Strip:", msg.strip())
print("Left strip:", msg.lstrip())
print("Right strip:", msg.rstrip())

# 7. Replacing Text
lang = "I like Java"
print("Replace Java with Python:", lang.replace("Java", "Python"))

# 8. Finding and Counting
text = "Learn Python Programming"
print("Find Python:", text.find("Python"))
print("Index of Python:", text.index("Python"))
print("Count of m:", text.count("m"))

# 9. Checking String Content
check = "Python123"
print("Is alphabet:", check.isalpha())
print("Is digit:", check.isdigit())
print("Is alphanumeric:", check.isalnum())
print("Is lowercase:", check.islower())
print("Is uppercase:", check.isupper())
print("Is title:", check.istitle())
print("Is space:", "   ".isspace())

# 10. Startswith and Endswith
word = "computer"
print("Starts with com:", word.startswith("com"))
print("Ends with ter:", word.endswith("ter"))

# 11. Splitting Strings
sentence = "Python is easy to learn"
words = sentence.split()
print("Split words:", words)

# 12. Joining Strings
joined = "-".join(words)
print("Joined string:", joined)

# 13. String Concatenation
a = "Hello"
b = "World"
print("Concatenated:", a + " " + b)

# 14. String Formatting
name = "Lakshmi"
age = 20
print("Using format(): Name is {} and age is {}".format(name, age))
print(f"Using f-string: Name is {name} and age is {age}")
