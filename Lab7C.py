n = int(input("amount of employees: "))
vacations = {}

for i in range(n):
    name, date = input("name and vacation date: ").split()
    month = date.split(".")[1]
    if month not in vacations:
        vacations[month] = []
    vacations[month].append(name)

search_month = input("search: ")
if search_month in vacations:
    print("employees who have vacation on this month:")
    print(*vacations[search_month], sep=" ")
else:
    print("no vacations(sad)")
