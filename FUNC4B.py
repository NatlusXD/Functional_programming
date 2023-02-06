students = []
while True:
    name = input("student name: ")
    if name == 'q':
        break
    grade = input("grade: ")
    students.append((name, int(grade)))


def get_grade(item):
    return item[1]


students.sort(key=get_grade)

for student in students:
    print("name: {}, grade: {}".format(student[0], student[1]))
