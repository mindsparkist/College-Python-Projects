# check Palindrom
def checkPalindrom(num):
    num = str(num)
    # 1234
    print(num[::-1])
    if num == num[::-1]:
        return True
    else:
        return False


userInput = int(input("Enter a number: "))
print(checkPalindrom(userInput))
