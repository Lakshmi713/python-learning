# 1. Simple Function (No arguments, no return)
def greet():
    print("Hello, Welcome to Python Functions")

greet()


# 2. Function with Arguments
def greet_user(name):
    print("Hello", name)

greet_user("Lakshmi")


# 3. Function with Multiple Arguments
def add(a, b):
    print("Sum:", a + b)

add(10, 20)


# 4. Function with Return Value
def square(num):
    return num * num

result = square(5)
print("Square:", result)


# 5. Function with Default Argument
def student(name, course="CSE"):
    print("Name:", name)
    print("Course:", course)

student("Lakshmi")
student("Lakshmi", "ML")


# 6. Function with Keyword Arguments
def details(name, age):
    print("Name:", name)
    print("Age:", age)

details(age=20, name="Lakshmi")


# 7. Function with Variable Length Arguments (*args)
def total(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print("Total:", sum)

total(10, 20, 30)
total(5, 15)


# 8. Function with Keyword Variable Length Arguments (**kwargs)
def profile(**info):
    for key, value in info.items():
        print(key, ":", value)

profile(name="Lakshmi", age=20, city="Nuzvid")


# 9 Function Calling Another Function
def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

sum_result = add(5, 3)
mul_result = multiply(sum_result, 2)
print("Final Result:", mul_result)


# 10. Recursive Function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
