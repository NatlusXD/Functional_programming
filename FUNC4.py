string = "Hello World"
length = len(string)
print("lenght is: ", length)
print()

number = 2020
string = str(number)
print("toString: ", string)
print()

string = "hello world"
upper_string = string.upper()
print("CAPS LOCK: ", upper_string)
print()

string = "HELLO WORLD"
lower_string = string.lower()
print("no caps lock: ", lower_string)
print()

string = "Hello World"
new_string = string.replace("World", "Friend")
print("replace: ", new_string)
print()

string = "Hello World"
splitted_string = string.split(" ")
print("split: ", splitted_string)
print()

list_of_strings = ["Hello", "World"]
joined_string = " ".join(list_of_strings)
print("join: ", joined_string)
print()

string = "Hello World"
index = string.find("World")
print("index of 'World' in : ", index)
print()

string = "Hello World"
starts_with = string.startswith("Hello")
print("starts with 'Hello': ", starts_with)
print()

string = "Hello World"
ends_with = string.endswith("World")
print("ends with 'World': ", ends_with)
print()
