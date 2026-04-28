
# num = int (input("Enter a no :"))
# if num > 0:
#     print("Number is integer")
# else:
#     print("Number is non integr")   

# num = int (input("Enter a no: "))
# if num > 0:
#     print("Number is Positive ")
# elif num < 0:
#     print("Number is Negative")
# else :
#     print("Number is zero")     

# age = int (input ("Enter a age: "))
# if age > 26 :
#     print (" You a adult ")
# elif age < 13 :
#     print("You a teen ")
# else :
#     print ("You are Genz")

# num = int (input ("Enter a no: "))
# if num %2 == 0 :
#     print ("No is Even")
# else :
#     print("No is Odd")

# a = int(input("Enter a no: "))
# b = int(input("Enter a no: "))
# c = int(input("Enter a no: "))
# if a >= b and a >= c:
#     print("a is largest")
# elif b >= a and b >= c:
#     print("b is largest")
# else:
#     print("c is largest")

# income = float(input("Enter a salary: "))
# if income < 250000:
#     tax = 0
# elif income <= 500000:
#     tax = income * 0.05
# elif income <= 1000000:
#     tax = income * 0.10
# else:
#     tax = income * 0.20
# print(tax)

# age = int(input("Enter a age: "))
# citizen = input("Enter a origin: ")
# if age > 18 :
#     if citizen == "India":
#         print(" You are elibilbe to vote ")
#     else :
#         print("You are not from India")
# else :
#     print("You cant vote")    
        
# m1 = int(input("Enter the marks: "))
# m2 = int(input("Enter the marks: "))
# m3 = int(input("Enter the marks: "))
# if m1 >= 35 and m2 >= 35 and m3 >= 35:
#     avg = (m1 + m2 + m3) / 3
#     if avg >= 75:
#         print("Distinction")
#     elif avg >= 60:
#         print("First Class")
#     else:
#         print("Pass")
# else:
#     print("Fail")

# rating = int(input("Enter rating upto 5: "))
# exp = int(input("Enter the experience: "))
# if rating >= 4:
#     if exp >= 5:
#         print("Promotion + Bonus")
#     else:
#         print("Bonus only")
# else:
#     if rating >= 3:
#         print("No promotion")
#     else:
#         print("Performance improvement required")

# amt = int(input("Enter an amout: "))
# loc = input("Enter a area ")
# if amt > 1000:
#     if loc == "local":
#         print("Free delivery")
#     else:
#         print("Delivery charge applied")
# else:
#     print("No free delivery")

# pwd = input("Enter a password: ")
# if len(pwd) >= 8:
#     if any(c.isdigit() for c in pwd):
#         if any(c.isupper() for c in pwd):
#             print("Strong password")
#         else:
#             print("Medium : use some special char ")
#     else:
#         print("Weak : use some number and upper case ")
# else:
#     print("Too short : Please enter more than 8 letters ")

# a = int(input("Enter a no: "))
# b = int(input("Enter a no: "))
# c = int(input("Enter a no: "))
# if a < b:
#     if b < c:
#         print("Strictly increasing")
#     else:
#         print("Not increasing")
# else:
#     print("Not increasing")

# num = int(input("Enter the no: "))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("Divisible by 6")
#     else:
#         print("Only divisible by 2")
# else:
#     if num % 3 == 0:
#         print("Only divisible by 3")
#     else:
#         print("Not divisible by 2 or 3")

# salary = int(input("Entre your salary: "))
# dept = input("Enter your dept. ")
# if dept == "IT":
#     if salary > 100000:
#         print("Senior Developer")
#     else:
#         print("Junior Developer")
# else:
#     if dept == "HR":
#         print("HR Staff")
#     else:
#         print("Other Department")

# number = int(input("Enter a no: "))

# if number % 3 == 0 and number % 5 == 0 :
#     print("FizzBuzz")
# elif number % 5 == 0:
#     print("Buzz")
# elif number % 3 == 0:
#     print("Fizz")
# else:
#     print("Invalid no : Divisible by other")

# num = float(input("Enter a number: "))

# if 0 <= num <= 50:
#     print("Range: 0–50")
# elif 51 <= num <= 100:
#     print("Range: 51–100")
# elif 101 <= num <= 200:
#     print("Range: 101–200")
# elif num > 200:
#     print("Range: Above 200")
# else:
#     print("Number is below 0")

# char = input("Enter a single character: ")

# if len(char) != 1:
#     print("Please enter only one character.")
# elif char.isupper():
#     print("Uppercase letter")
# elif char.islower():
#     print("Lowercase letter")
# elif char.isdigit():
#     print("Digit")
# else:
#     print("Special character")

a = float(input("Side A: "))
b = float(input("Side B: "))
c = float(input("Side C: "))

# Physical Validation: Sum of any two sides must be greater than the third
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("These sides cannot form a valid triangle.")