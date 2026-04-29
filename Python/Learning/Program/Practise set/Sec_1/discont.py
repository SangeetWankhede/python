
# price = int (input("Eter the price: "))
# disscount = int (input("Enter the disscount in %: "))

# disscount_price = price * disscount // 100

# final_price = price - disscount_price

# print("Final amount will be ", final_price)

num = int(input("Enter a 3-digit number: "))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

sum_digits = d1 + d2 + d3

print("Sum of digits:", sum_digits)