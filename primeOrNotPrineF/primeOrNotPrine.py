# Prime Or Not Prime
def primeOrNotPrime(n):
    if n == 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"


userInput = int(input("Enter a number: "))
print(primeOrNotPrime(userInput))
