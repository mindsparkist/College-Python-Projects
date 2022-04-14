x = int(input('Enter a binary number:'))
s = 0
n = x
a = 1
while (n != 0):
    r = int(n % 10)
    s = int(s+r*a)
    n = int(n/10)
    a = int(a*2)

print(f"After binary to decimal:{x} to {s}")
