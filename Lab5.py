# students = []
# while True:
#     name = input("Введите имя студента или нажмите Enter, чтобы закончить: ")
#     if name == "":
#         break
#     group = input("Введите группу студента: ")
#     students.append((name, group))
#
# students_sorted = sorted(students, key=lambda x: x[1])
# for student in students_sorted:
#     print(f"{student[0]} ({student[1]})")



# grades = {
#     "Иванов": {"математика": 4, "русский язык": 5, "английский язык": 3},
#     "Петров": {"математика": 5, "русский язык": 4, "английский язык": 4},
#     "Сидоров": {"математика": 3, "русский язык": 4, "английский язык": 5},
# }
#
# student_name = input("Введите имя учащегося: ")
# if student_name in grades:
#     for subject, grade in grades[student_name].items():
#         print(f"{subject}: {grade}")
# else:
#     print("Такого учащегося нет в списке.")


# numbers = []
# while True:
#     num = int(input("Введите целое число или 0 для завершения: "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# numbers_sorted = sorted(numbers)
# for num in numbers_sorted:
#     print(num)



# numbers = []
# while True:
#     num = int(input("Введите целое число или 0 для завершения: "))
#     if num == 0:
#         break
#     numbers.append(num)
#
# numbers_sorted = sorted(numbers, reverse=True)
# for num in numbers_sorted:
#     print(num)



# import random
#
# # Generate 6 unique numbers between 1 and 49
# numbers = random.sample(range(1, 50), 6)
#
# # Sort the numbers in ascending order
# numbers.sort()
#
# # Print the numbers
# print(numbers)



# def is_sorted(lst):
#     return lst == sorted(lst) or lst == sorted(lst, reverse=True)
#
# # Prompt the user to enter a list of integers
# lst = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
#
# # Check if the list is sorted and print the result
# if is_sorted(lst):
#     print("The list is sorted.")
# else:
#     print("The list is not sorted.")