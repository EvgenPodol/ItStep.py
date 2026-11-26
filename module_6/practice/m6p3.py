# Завдання 1
# Створіть список чисел [1, 8, -5, 9]
# ● Виведіть на екран елементи цього списку
# ● Збільшіть кожне число в 3 рази та виведіть результат
# ● Замініть усі числа більші 10 на 0 та виведіть
# результат

# numbers = [1, 8, -5, 9]
#
# for n in numbers:
#     print(n)
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 3
# print("Помножені на 3:", numbers)
#
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#         numbers[i] = 0
# print("Після заміни:", numbers)

# Завдання 2
# Користувач вводить числа, поки не введе -1.
# Збережіть усі ці числа в список. Виведіть їхню кількість,
# суму, мінімальне, максимальне та середнє.
# Скористайтесь функціями min, max, sum, len

# numbers = []
# n = float(input("Введіть число (-1 для завершення): "))
# while True:
#     numbers.append(n)
#     n = float(input("Введіть число (-1 для завершення): "))
#     if len(numbers) > 0:
#         print("Кількість:", len(numbers))
#         print("Сума:", sum(numbers))
#         print("Мінімум:", min(numbers))
#         print("Максимум:", max(numbers))
#         print("Середнє:", sum(numbers) / len(numbers))
#     else:
#         print("Жодного числа не введено")

# Завдання 3
# Користувач вводить числа, поки не введе 0. Створіть
# два нових списки: з додатніми та від’ємними числами.
# Виведіть елементи обох списків на екран.
# Виправіть помилку в коді

# positive = []
# negative = []
#
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     if number < 0:
#         negative.append(number)
#     else:
#         positive.append(number)
#
#     print("Додатні числа:", positive)
#     print("Від'ємні числа:", negative)
