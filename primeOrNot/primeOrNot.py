x = int(input("Enter a number: "))
for i in range(2, x):
    if x % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")
