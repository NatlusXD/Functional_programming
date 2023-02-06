while True:
    num1 = input("first number: ")
    num2 = input("second number: ")

    if num1.isdigit() and num2.isdigit():
        print("sum:", int(num1) + int(num2))
        break
    else:
        print("no")