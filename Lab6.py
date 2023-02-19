# # Создание кортежа со списком резюме студентов
# resumes = (
#     ("John Doe", "Computer Science", "Internship", "Skills: Python, Java"),
#     ("Jane Smith", "Marketing", "Entry-level position", "Skills: Social media marketing, Adobe Photoshop"),
#     ("Bob Johnson", "Business Administration", "Management trainee", "Skills: Leadership, Strategic planning"),
#     ("Sarah Lee", "Journalism", "Reporter", "Skills: Writing, Interviewing"),
#     ("David Kim", "Data Science", "Data Analyst", "Skills: Data analysis, Machine learning")
# )
#
# # Преобразование кортежа в множество
# resumes_set = set(resumes)
#
# # Функция, которая возвращает количество резюме в кортеже
# def count_resumes(resumes):
#     return len(resumes)
#
# # Функция, которая выводит все резюме в кортеже
# def print_resumes(resumes):
#     for resume in resumes:
#         print(resume)
#
# # Функция, которая возвращает только те резюме, которые имеют в названии заданную должность
# def filter_by_position(resumes, position):
#     filtered_resumes = []
#     for resume in resumes:
#         if position in resume[2]:
#             filtered_resumes.append(resume)
#     return tuple(filtered_resumes)
#
# # Функция, которая возвращает только те резюме, которые имеют в названии заданный навык
# def filter_by_skill(resumes, skill):
#     filtered_resumes = []
#     for resume in resumes:
#         if skill in resume[3]:
#             filtered_resumes.append(resume)
#     return tuple(filtered_resumes)
#
# # Функция, которая проверяет, есть ли заданное резюме в множестве резюме
# def check_resume(resume, resumes_set):
#     return resume in resumes_set
#
# # Пример использования функций
# print("Количество резюме:", count_resumes(resumes))
# print("\nВсе резюме:")
# print_resumes(resumes)
#
# position = "Data"
# print("\nРезюме для должности '{}'".format(position))
# position_resumes = filter_by_position(resumes, position)
# print_resumes(position_resumes)
#
# skill = "Java"
# print("\nРезюме с навыком '{}'".format(skill))
# skill_resumes = filter_by_skill(resumes, skill)
# print_resumes(skill_resumes)
#
# resume = ("John Doe", "Computer Science", "Internship", "Skills: Python, Java")
# if check_resume(resume, resumes_set):
#     print("\nРезюме {} найдено в множестве резюме".format(resume))
# else:
#     print("\nРезюме {} не найдено в множестве резюме".format(resume))



# import random
#
# def generate_tuple():
#     tuple1 = tuple(random.randint(0, 5) for _ in range(10))
#     tuple2 = tuple(range(5, -1, -1))
#     return tuple1, tuple2
#
# tuple1, tuple2 = generate_tuple()
# tuple3 = tuple1 + tuple2
# zeros_count = tuple3.count(0)
#
# print("Tuple 1:", tuple1)
# print("Tuple 2:", tuple2)
# print("Tuple 3:", tuple3)
# print("Number of zeros in Tuple 3:", zeros_count)



# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# categories = ["Transportation", "Lunch", "Groceries", "Entertainment"]
# expenses = []
# for day in weekdays:
#     daily_expenses = {}
#     for category in categories:
#         amount = float(input(f"Enter amount spent on {category} on {day}: "))
#         daily_expenses[category] = amount
#     expenses.append(daily_expenses)
#
# for i, day in enumerate(weekdays):
#     total_expenses = sum(expenses[i].values())
#     print(f"Total expenses for {day}: ${total_expenses:.2f}")
#
# total_weekly_expenses = sum(sum(day_expenses.values()) for day_expenses in expenses)
# print(f"Total weekly expenses: ${total_weekly_expenses:.2f}")



# names_input = input("Enter student names separated by spaces: ")
# names_tuple = tuple(names_input.split())
# names_with_va = [name for name in names_tuple if "va" in name]
# print("Names with 'va':", " ".join(names_with_va))



# mapping = {
#     'а': 'a', 'ә': 'á', 'б': 'b', 'в': 'v', 'г': 'g', 'ғ': 'ǵ',
#     'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'j', 'з': 'z', 'и': 'ı',
#     'й': 'ı', 'к': 'k', 'қ': 'q', 'л': 'l', 'м': 'm', 'н': 'n',
#     'ң': 'ń', 'о': 'o', 'ө': 'ó', 'п': 'p', 'р': 'r', 'с': 's',
#     'т': 't', 'у': 'ý', 'ұ': 'u', 'ү': 'ú', 'ф': 'f', 'х': 'h',
#     'һ': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
#     'ы': 'y', 'і': 'i', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
# }
#
# def kazakh_cyrillic_to_latin(text):
#     result = []
#     for char in text:
#         if char.lower() in mapping:
#             if char.isupper():
#                 result.append(mapping[char.lower()].capitalize())
#             else:
#                 result.append(mapping[char])
#         else:
#             result.append(char)
#     return ''.join(result)
#
# text = 'Сәлем, әлем! Менің атым Кира Йощикагэ. Мен Қазақстаннан келем.'
# print(kazakh_cyrillic_to_latin(text))
