x = int(input("Enter a number: "))
sum = 0
while x > 0:
    sum = sum + x % 10
    x = x // 10
print(f"Sum of digits of entered number is: {sum}")
