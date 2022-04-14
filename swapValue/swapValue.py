# swap two values
firstValue = int(input("Enter first value: "))
secondValue = int(input("Enter second value: "))
print(
    f"Before swapping: Firstvalue is  {firstValue} and Secondvalue is {secondValue}")
# its done by using the tupple unpacking
firstValue, secondValue = secondValue, firstValue
print(
    f"After swapping: Firstvalue is  {firstValue} and Secondvalue is {secondValue}")
