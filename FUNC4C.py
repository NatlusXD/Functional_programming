strInput = input("Input: ")

upper = 0
lower = 0

for char in strInput:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

if upper > lower:
    output = strInput.upper()
else:
    output = strInput.lower()

print("Output:", output)
