# Convert decimal to binary
def decimalToBinary(decimal):
    binary = ''
    while decimal > 0:
        # Append the remainder to the binary string
        binary = str(decimal % 2) + binary
        decimal = decimal // 2  # integer division to remove decimal part
    return binary


userInput = int(input('Enter a decimal number: '))
print(decimalToBinary(userInput))
