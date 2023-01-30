import random

# randint
dice_roll = random.randint(1, 6)
print(dice_roll)
print(" ")

# randrange
even_number = random.randrange(10, 20, 2)
print(even_number)
print(" ")

# random with float
random_float = random.random()
print(random_float)
print(" ")

# enumerate
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
print(" ")

# Даны два целых числа A и B (при этом A ≤ B).
# Выведите все числа от A до B включительно
A = 5
B = 10
for i in range(A, B + 1):
    print(i)
print(" ")

# Даны два целых числа A и В. Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B, или в порядке убывания в противном случае.
A = 10
B = 5
if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)
print(" ")

# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно,
# в порядке убывания. В этой задаче можно обойтись без инструкции if.
A = 11
B = 5
while A % 2 == 0:
    A -= 1
for i in range(A, B - 1, -2):
    print(i)
print(" ")

numbers = list(range(1, 11))
print(numbers)
