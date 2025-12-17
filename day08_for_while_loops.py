"""
FOR LOOP:
A for loop is used to iterate over a sequence such as a list, tuple, set,
string, or range. It is mainly used when the number of iterations is known
in advance.

WHILE LOOP:
A while loop is used to execute a block of code repeatedly as long as a
given condition is true. It is mainly used when the number of iterations
is not known in advance.
"""

# ---------------- FOR LOOP ----------------

# 1. Print numbers from 1 to 5
print("For Loop: Numbers from 1 to 5")
for i in range(1, 6):
    print(i)

# 2. Print even numbers from 1 to 10
print("\nFor Loop: Even numbers from 1 to 10")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 3. Sum of numbers from 1 to 5
total = 0
for i in range(1, 6):
    total += i
print("\nFor Loop: Sum from 1 to 5 =", total)

# 4. Print elements of a list
fruits = ["apple", "banana", "mango"]
print("\nFor Loop: Fruits list")
for fruit in fruits:
    print(fruit)

# 5. Multiplication table of 5
print("\nFor Loop: Table of 5")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# ---------------- WHILE LOOP ----------------

# 6. Print numbers from 1 to 5
print("\nWhile Loop: Numbers from 1 to 5")
i = 1
while i <= 5:
    print(i)
    i += 1

# 7. Print odd numbers from 1 to 10
print("\nWhile Loop: Odd numbers from 1 to 10")
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 8. Reverse counting from 5 to 1
print("\nWhile Loop: Reverse counting")
i = 5
while i >= 1:
    print(i)
    i -= 1

# 9. Sum of numbers from 1 to 5
total = 0
i = 1
while i <= 5:
    total += i
    i += 1
print("\nWhile Loop: Sum from 1 to 5 =", total)

# 10. Simple password check
password = "1234"
entered_password = "1234"

while entered_password != password:
    print("Wrong Password")
    entered_password = "1234"

print("\nWhile Loop: Login Successful")
