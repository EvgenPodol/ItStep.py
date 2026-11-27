# Завдання 1
# Користувач вводить рядок та символ. Порахуйте скільки
# разів цей символ зустрічається у рядку.
# Зробіть двома способами:
# ● з методом count
# ● з циклом for
# Приклад:
# В “it is amazing” символ “і” зустрічається 3 рази

# text = input("введіть текст: ")
# symbol = input("введіть символ: ")
# count = 0
#
# for ch in text:
#     if ch == symbol:
#         count += 1
# print(f"літера {symbol} зустрілась  {count} разів")

# Другий спосіб

# text = input("введіть текст: ")
# symbol = input("введіть символ: ")
#
# print(text.count(symbol))

# Завдання 2
# Користувач вводить рядок. Виведіть наступну
# інформацію:
# ● кількість символів
# ● чи є там слово python
# ● кількість шиплячих літер – szh

# text = input("введіть текст: ")
#
# szh = 0
# for ch in text:
#     if ch in "жчшщЖЧШЩ":
#         szh += 1
#
# print("Кількість символів:", len(text))
# print("Кількість шиплячих літер:", szh)
# print("слово python", "python" in text)

# Завдання 3
# Користувач вводить тест. Потрібно замінити всі пробіли
# на дефіси. Виправіть помилку в коді

# text = input("Введіть текст: ")
#
# print(f"Змінений текст: {text.replace(" ", "-")}")

# Завдання 4
# Користувач вводить рядок та слово. Порахуйте скільки
# разів це слово зустрічається у рядку

# text = input("Введіть рядок: ")
# word = input("Введіть слово: ")
#
# print(f"Слово «{word}» зустрічається {text.count(word)} раз(и)")

# Завдання 5
# При оформлені посилки заборонено перевозити
# наступні речі:
# ● ножі
# ● гроші
# ● сильні отрути
# Виправіть помилку в коді

# items = input("Введіть ваші речі: ").lower()
#
# if "ніж" in items or "гроші" in items or "отрута" in items:
#     print("У вас є речі які заборонено перевозити")
# else:
#     print("Оформлено доставку")

# Завдання 6
# Користувач вводить текст. Порахуйте скільки в ньому
# літер та цифр.

# text = input("Enter a text: ")
#
# letters = 0
# numbers = 0
#
# for char in text:
#     if char.isdigit():
#         numbers += 1
#     elif char.isalpha():
#         letters += 1
#
# print("кількість літер: ", letters)
# print("кількість цифр: ", numbers)

# Завдання 7
# Користувач вводить пароль поки не введе його
# правильно.
# Правильний пароль повинен:
# ● Бути довшим за 8 символів
# ● Містити хоча б одну цифру
# ● Містити хоча б одну літеру

password = input("Enter your password: ")

count_number = 0
count_letter = 0
count_symbol = 0

for s in password:
    if s.isalpha():
        count_letter += 1
    if s.isdigit():
        count_number += 1
    if len(password):
        count_symbol += 1

if count_letter >= 1 and count_number >= 1 and count_symbol >= 8:
    print("Дуже добрий пароль")
else:
    print("Поганий пароль")
