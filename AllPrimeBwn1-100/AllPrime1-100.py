lowerbound = int(input("Enter the lowerbound: "))
upperbound = int(input("Enter the upperbound: "))
for num in range(lowerbound, upperbound+1):
    if num > 1:  # All prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
