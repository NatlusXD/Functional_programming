n = int(input("amount of lmn: "))
rivers = {}
for i in range(n):
    country, river = input("country and river: ").split()
    rivers[river] = country

print("for each river there is a country:")
for river, country in rivers.items():
    print(f"{river} - {country}")

search_river = input("river search: ")
if search_river in rivers:
    print("there is a river: ")
else:
    print("there is no such river: ")

new_country, new_river = input("add country and river: ").split()
rivers[new_river] = new_country
print("new country/river has been added:")
for river, country in rivers.items():
    print(f"{river} - {country}")
