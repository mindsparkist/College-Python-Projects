import math as mth
sum = 0
X = int(input("Enter the value of X: "))
N = int(input("Enter the value of N: "))
k = 1
for i in range(1, N+1):
    if i % 2 == 0:
        sum = sum - (X**k)/mth.factorial(k)
    else:
        sum = sum + (X**k)/mth.factorial(k)
    k = k + 2
print("The sum of the series is: ", sum)
