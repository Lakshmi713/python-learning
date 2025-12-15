# Python if–elif–else Statements – Basic Programs

# 1. Grade Calculation
marks = 78

if marks >= 90:
    print("1. Grade: A")
elif marks >= 75:
    print("1. Grade: B")
elif marks >= 60:
    print("1. Grade: C")
elif marks >= 40:
    print("1. Grade: D")
else:
    print("1. Fail")

# 2. Largest of Three Numbers
a = 25
b = 40
c = 30

if a >= b and a >= c:
    print("2. a is largest")
elif b >= a and b >= c:
    print("2. b is largest")
else:
    print("2. c is largest")

# 3. Check Number Type
num = -5

if num > 0:
    print("3. Positive Number")
elif num < 0:
    print("3. Negative Number")
else:
    print("3. Zero")

# 4. Day Name Using Number
day = 3

if day == 1:
    print("4. Monday")
elif day == 2:
    print("4. Tuesday")
elif day == 3:
    print("4. Wednesday")
elif day == 4:
    print("4. Thursday")
elif day == 5:
    print("4. Friday")
elif day == 6:
    print("4. Saturday")
elif day == 7:
    print("4. Sunday")
else:
    print("4. Invalid Day")

# 5. Simple Calculator
a = 10
b = 5
choice = 3   # 1:Add  2:Sub  3:Mul  4:Div

if choice == 1:
    print("5. Addition:", a + b)
elif choice == 2:
    print("5. Subtraction:", a - b)
elif choice == 3:
    print("5. Multiplication:", a * b)
elif choice == 4:
    print("5. Division:", a / b)
else:
    print("5. Invalid Choice")

# 6. Age Category
age = 16

if age < 13:
    print("6. Child")
elif age < 20:
    print("6. Teenager")
elif age < 60:
    print("6. Adult")
else:
    print("6. Senior Citizen")

# 7. Traffic Light
signal = "green"

if signal == "red":
    print("7. Stop")
elif signal == "yellow":
    print("7. Ready")
elif signal == "green":
    print("7. Go")
else:
    print("7. Invalid Signal")
