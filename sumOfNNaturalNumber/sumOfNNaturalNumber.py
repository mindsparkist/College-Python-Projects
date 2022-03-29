# Sum Of N Natural Number
def sumOfNNaturalNumber(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum


userInput = int(input("Enter a number: "))
print(sumOfNNaturalNumber(userInput))
