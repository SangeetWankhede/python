# # r = float(input("Enter the radius: "))
# # # pi = 3.14
# # area = 3.14*r*2
# # print("Area of circle",area)

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate(%): ")) 
# time = float(input("Enter the time(in year): "))

# simple_intrest = (principal*rate*time)/100
# total_amount = principal + simple_intrest
# # # print("Simpe intrest is",simple_intrest)
# # # Standard Simple Interest Formula: (P * R * T) / 100
# # principal = float(input("Enter the principal amount: "))
# # rate = float(input("Enter the annual interest rate (%): ")) 
# # time = float(input("Enter the time (in years): "))

# # # Calculation
# # simple_interest = (principal * rate * time) / 100
# # total_amount = principal + simple_interest

# print("-" * 30)
# print(f"Simple Interest: {simple_intrest:.2f}")
# print(f"Total Balance:   {total_amount:.2f}")
# print("-" * 30)

# english = 76
# hindi = 74
# marathi = 80
# science = 90
# maths = 100

# total_mark = (english+hindi+marathi+science+maths)

# percentage = total_mark/5 * 100

# print("Avrgare of marks",total_mark)
# print("Percentile ",percentage)

english = 76
hindi = 74
marathi = 80
science = 90
maths = 100

# Step 1: Sum the marks
total_obtained = english + hindi + marathi + science + maths

# Step 2: Calculate Average (Total / 5 subjects)
average = total_obtained / 5

# Step 3: Calculate Percentage ( (Total / 500) * 100 )
# Note: Since there are 5 subjects out of 100, (total/500)*100 is the same as total/5
percentage = (total_obtained / 500) * 100

print("Total Marks:   ", total_obtained)
print("Average Marks: ", average)
print(f"Percentage:    {percentage}%")