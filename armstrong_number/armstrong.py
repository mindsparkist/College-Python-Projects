x = int(input("Enter a number: "))
org_x = x
sum = 0
while x > 0:
    rem = x % 10
    sum += rem ** 3  # rem ^ 3
    x //= 10  # give the value before the decimal point
if sum == org_x:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
