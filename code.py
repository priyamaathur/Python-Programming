# print("Hii!", " I am Priya Mathur")

# variables 
"""
name = 'Priya Mathur'
age = 21
#print(name, age)
name = 'Mathur '
age = 22
cgpa = 7.7
isStudent = True
print(name, age, cgpa)

print(type(name))
print(type(cgpa))
print(type(isStudent))
"""

# input function
"""
name = input("Enter your name: ")
print("Hello " + name) #concatenation
print("Hello", name) #comma separated
"""
#exercise 1
"""
first_name = "Tony"
last_name  = "Stark"
age = 53
height = "1.85m"
details = print("My name is " + first_name + " " + last_name + ". I am " + str(age) + " years old and my height is " + height + ".")

secret = input("Enter your secret: ")
print("Tony stark is secretly a " + secret + ".")
"""

#type conversion
"""
age = (input("Enter your age: ")) # string input 
print(type(age))
age = int(age) # type conversion to integer
print(type(age))
"""

# sum program 
"""
a = int(input("enter a: "))
b = int(input("enter b: "))
sum = a + b 
print("sum:" , sum ) 
"""

#string methods
""" 

s = 'My name is Priya Mathur'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

print(s.swapcase())
print(s.find('Priya'))
print(s.index('Mathur'))
print(s.count('a'))
print(s.replace('Priya', 'Ananya'))
print(s.startswith('My'))
print(s.endswith('Mathur'))
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.split())
print(s.join(['Hello', 'World']))

"""

#exercise-2 
"""

# 1. take price of products as input and print the total bill and average price 

p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
total_bill = p1 + p2 + p3
average_price = total_bill /3 
print("Total bill : ", total_bill)
print("Average price : ", average_price)

# 2. take a superhero name as input  and check it start with s / S or not 
name = input("Enter a superhero name: ")
print(name.startswith('s') or name.startswith('S'))
"""

# conditional statements
"""
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    """
    
    # Mini project - 1 (Calculator)
    
"""
a = float(input("Enter first number: "))
select_operation = input("Select operation (+, -, *, /, % , **): ")
b = float(input("Enter second number: "))
if select_operation == '+':
    print("Result: ", a + b)
elif select_operation == '-':
    print("Result: ", a - b)
elif select_operation == '*':
    print("Result: ", a * b)
elif select_operation == '/':
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result: ", a / b)
elif select_operation == '%':
    print("Result: ", a % b)
elif select_operation == '**':
    print("Result: ", a ** b)
else:
    print("Invalid operation.")

"""

# range and loops 
"""
for i in range(1, 11):
    print(i)
    
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    print("You entered:", num)
  
  # continue statement
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)  
"""

# Practice exercise - 4
# print odd numbers from 1 to 20 
"""
for i in range(1, 21, 2):
    print(i)
"""

# print table of 57
"""
i= 1
for i in range(1, 11):
    print("57 x", i, "=", 57 * i)
"""
# print all  multiples of 3 from 1 to 50 but skip 15
"""
for i in range(1, 51):
    if i % 3 == 0:
        if i == 15:
            continue
        print(i)
"""
# take two integer aas input and find he first number 1 and 1000 is divisible by both numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print("First number divisible by both:", i)
        break



