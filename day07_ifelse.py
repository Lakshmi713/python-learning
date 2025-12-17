# Python if–else Statements – Basic Programs

# 1. Positive or Negative
num = 10
if num > 0:
    print("1. Number is Positive")
else:
    print("1. Number is Negative")

# 2. Even or Odd
num = 7
if num % 2 == 0:
    print("2. Even Number")
else:
    print("2. Odd Number")

# 3. Voting Eligibility
age = 20
if age >= 18:
    print("3. Eligible to Vote")
else:
    print("3. Not Eligible to Vote")

# 4. Compare Two Numbers
a = 15
b = 10
if a > b:
    print("4. a is greater than b")
else:
    print("4. b is greater than a")

# 5. Largest of Three Numbers
a = 10
b = 20
c = 15

if a >= b and a >= c:
    print("5. a is largest")
elif b >= a and b >= c:
    print("5. b is largest")
else:
    print("5. c is largest")

# 6. Pass or Fail
marks = 45
if marks >= 40:
    print("6. Pass")
else:
    print("6. Fail")

# 7. Leap Year Check
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("7. Leap Year")
else:
    print("7. Not a Leap Year")

# 8. Simple Login Check
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("8. Login Successful")
else:
    print("8. Login Failed")
