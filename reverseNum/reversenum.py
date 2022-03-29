x = int(input("Enter a number: "))
reverse = 0
while x > 0:
    reverse = reverse * 10
    reverse = reverse + x % 10
    x = x // 10
print(f"Reverse of entered number is: {reverse}")
