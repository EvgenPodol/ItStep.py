# Завдання 1
# Користувач вводить число від 1 до 9. Потрібно вивести
# для цього числа таблицю множення.
# Наприклад для 5 це буде:
# 1х5=5
# 2х5=10
# …
# 9х5=45
# 10х5=50
# Якщо користувач ввів неправильне число то
# продовжувати запитувати поки не введе правильне.


# while True:
#     num = int(input("Введіть число від 1 до 9: "))
#     if 1 <= num <= 9:
#         for i in range(1, 11):
#             print(f"{i} * {num} = {i * num}")
#         break
#     else:
#         print("Помилка! Потрібно ввести число саме від 1 до 9. Спробуйте ще раз.")

# Завдання 2
# Користувач вводить свої оцінки поки не введе 0. Після
# чого програма виводить середню оцінку

# total = 0
# count = 0
#
# while True:
#     grade = int(input("Введіть оцінку: "))
#
#     if grade == 0:
#         if count > 0:
#             average_grade = total / count
#             print(f"середня оцінка: {average_grade:.1f}")
#         else:
#             print("Ви не ввели жодної оцінки.")
#         break
#     else:
#         count += 1
#         total += grade

# Завдання 3
# Напишіть простий калькулятор
# Користувач вводить два числа після чого обирає яку дію
# виконати:
# 1. сума
# 2. різниця
# 3. добуток
# 4. частка
# 5. вихід
# Якщо користувач обрав частку, то переконайтесь що не
# буде ділення на 0. У випадку проблеми виведіть відповідне
# повідомлення.
#
# num1 = int(input("Введіть число: "))
# num2 = int(input("Введіть інше число: "))

# while True:
#     print("Введіть дію: \n 1.сума \n 2.різниця \n 3.добуток \n 4.частка \n 5.вихід")
#     action = input("Ваш вибір: ")
#     if action == "сума":
#         result = num1 + num2
#         print(result)
#         break
#     elif action == "різниця":
#         if num1 > num2:
#             result = num1 - num2
#             print(result)
#         else:
#             num1, num2 = num2, num1
#             result = num1 - num2
#             print(result)
#     elif action == "добуток":
#         result = num1 * num2
#         print(result)
#     elif action == "частка":
#         if num1 != 0 and num2 != 0:
#             if num1 > num2:
#                 result = num1 / num2
#                 print(result)
#             else:
#                 num1, num2 = num2, num1
#                 result = num1 / num2
#                 print(result)
#         else:
#             print("неможливо поділити0")
#     elif action == "вихід":
#         print("До побачення")
#         break

# Завдання 4
# Програма повинна зареєструвати рівно 3 учасників. Для
# цього користувач вводить їхні імена, але ім’я admin уже
# зайняте

# count = 0
#
# while count < 3:
#     name = input("Введіть ім'я: ")
#     if name == "admin":
#         print("Це ім'я недоступне")
#     else:
#         count += 1
#         print(f"Учасник №{count}: {name}")

# Завдання 4
# Напишіть гру «Вгадай число».
# Користувач має відгадати число від 0 до 100. Коли
# користувач пропонує власне число, програма має вивести
# одне з повідомлень:
# ● Замало
# ● Забагато
# ● Ви вгадали(кінець програми)
# Після того як користувач відгадав число треба показати
# скільки у нього пішло на це спроб.
# Також якщо користувач вводить замість числа слово
# stop, програма показує число та кількість спроб і припиняє
# роботу.
# Для того щоб згенерувати випадкове число на початку
# програми напишіть
# import random
# А вже в місці де потрібно згенерувати число:
# secret_num = random.randint(0, 100)

# import random
#
# secret_num = random.randint(0, 100)
# attempts = 0
#
# while True:
#     answer = input("Введіть число від 0 до 100 (або stop): ")
#
#     if answer == "stop":
#         print(f"Загадане число: {secret_num}")
#         print(f"Кількість спроб: {attempts}")
#         break
#
#     number = int(answer)
#     attempts += 1
#
#     if number < secret_num:
#         print("Замало")
#     elif number > secret_num:
#         print("Забагато")
#     else:
#         print("Ви вгадали!")
#         print(f"Кількість спроб: {attempts}")
#         break

# Завдання 5
# Напишіть гру «Камінь, ножиці, папір»
# Спочатку користувач пропонується вибір:
# 1. Нова гра
# 2. Вихід
# Якщо вибрана нова гра, то користувач вводить кількість
# раундів.
# На кожному раунді користувач вводить одне зі слів:
# «камінь», «ножиці» або «папір». Якщо користувач вводить
# щось інше, зарахуйте це як програш в раунді.
# Коли всі раунди закінчились потрібно вивести кількість
# перемог, програшів та нічиї.
# Щоб згенерувати вибір комп’ютера використайте такий
# код

# import random
#
# print("1. Нова гра")
# print("2. Вихід")
# choice = input("Ваш вибір: ")
#
# if choice == "1":
#     rounds = int(input("Скільки раундів? "))
#     wins = 0
#     losses = 0
#     draws = 0
#
#     for i in range(rounds):
#         user = input("камінь, ножиці або папір: ")
#         computer = random.choice(["камінь", "ножиці", "папір"])
#         print(f"Комп'ютер обрав: {computer}")
#
#         if user not in ["камінь", "ножиці", "папір"]:
#             print("Некоректне слово, раунд програно")
#             losses += 1
#         elif user == computer:
#             print("Нічия")
#             draws += 1
#         elif (user == "камінь" and computer == "ножиці") or \
#              (user == "ножиці" and computer == "папір") or \
#              (user == "папір" and computer == "камінь"):
#             print("Ви виграли раунд")
#             wins += 1
#         else:
#             print("Ви програли раунд")
#             losses += 1
#
#     print(f"Перемог: {wins}")
#     print(f"Програшів: {losses}")
#     print(f"Нічиїх: {draws}")

# авдання 6
# Змініть завдання 5 так, щоб на можна було грати
# декілька ігор.
# Для цього програма пропонує вибір:
# 1. Нова гра
# 2. Вихід

import random

while True:
    print("\n1. Нова гра")
    print("2. Вихід")
    choice = input("Ваш вибір: ")

    if choice == "2":
        print("До побачення!")
        break

    if choice == "1":
        rounds = int(input("Скільки раундів? "))
        wins = 0
        losses = 0
        draws = 0

        for _ in range(rounds):
            user = input("камінь, ножиці або папір: ")
            computer = random.choice(["камінь", "ножиці", "папір"])
            print(f"Комп'ютер обрав: {computer}")

            if user not in ["камінь", "ножиці", "папір"]:
                print("Некоректне слово, раунд програно")
                losses += 1
            elif user == computer:
                print("Нічия")
                draws += 1
            elif (
                (user == "камінь" and computer == "ножиці")
                or (user == "ножиці" and computer == "папір")
                or (user == "папір" and computer == "камінь")
            ):
                print("Ви виграли раунд")
                wins += 1
            else:
                print("Ви програли раунд")
                losses += 1

        print(f"Перемог: {wins}")
        print(f"Програшів: {losses}")
        print(f"Нічиїх: {draws}")
    else:
        print("Оберіть 1 або 2")
