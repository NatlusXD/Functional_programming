print("enter amount of lmns")
n = int(input())

phone_book = {}

print("enter names and numbers")
for i in range(n):
    phone, name = input().split()
    phone_book[name] = phone

print("enter a query")
queryN = input()

if queryN in phone_book:
    print(phone_book[queryN])
else:
    print("there is nothing")
