students = {'Jojo': {'age': 22, 'degree': 'alchemy', 'GPA': 3.7},
            'Jotaro': {'age': 21, 'degree': 'meth', 'GPA': 3.9},
            'Jonathan': {'age': 20, 'degree': 'mining', 'GPA': 3.2},
            'Joseph': {'age': 23, 'degree': 'gaming', 'GPA': 3.5},
            'Jolin': {'age': 24, 'degree': 'cooking', 'GPA': 3.8}}


def getInfo(students_dict):
    for name, info in students_dict.items():
        print(f"Name: {name}\nAge: {info['age']}\nDegree: {info['degree']}\nGPA: {info['GPA']}\n")


def add(students_dict):
    name = input("student name: ")
    age = int(input("student age: "))
    degree = input("student degree: ")
    gpa = float(input("student gpa: "))
    students_dict[name] = {'age': age, 'degree': degree, 'GPA': gpa}


def delete(students_dict):
    name = input("Enter student name to delete: ")
    if name in students_dict:
        del students_dict[name]
    else:
        print("not found")


def update(students_dict):
    name = input("name to update: ")
    if name in students_dict:
        age = int(input("student age: "))
        degree = input("student degree: ")
        GPA = float(input("student gpa: "))
        students_dict[name] = {'age': age, 'degree': degree, 'GPA': GPA}
    else:
        print("not found")


def search(students_dict):
    name = input("search by name: ")
    if name in students_dict:
        getInfo({name: students_dict[name]})
    else:
        print("not found")


add(students)
getInfo(students)

delete(students)
getInfo(students)

update(students)
getInfo(students)

search(students)
