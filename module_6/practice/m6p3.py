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

# Завдання 4
# Користувач вводить зарплати співробітників, поки не
# введе -1. Після чого вводить відсоток на який треба
# збільшити усім зарплату.
# Виведіть нові зарплати

# salaries = []
#
# while True:
#     salary = float(input("Введіть зарплату (-1 для завершення): "))
#     if salary <0:
#         break
#     salaries.append(salary)
#
#     percent = float(input("На скільки відсотків збільшити зарплату? "))
#
#     new_salaries = []
#     for salary in salaries:
#         new_salaries.append(salary * (1 + percent / 100))
#
#     print("Нові зарплати:")
#     for salary in new_salaries:
#         print(salary)

# Завдання 5
# Користувач вводить кількість днів, після чого
# температуру повітря кожного дня.
# Збережіть температури у список
# Для кожного дня порахуйте різницю температур з
# попереднім днем.
# Виправіть помилку в коді

# days = int(input("Введіть кількість днів: "))
# temperatures = []
#
# for i in range(days):
#
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)
#
# print("Температури:", temperatures)
#
# for i in range(days):
#     if i != 0:
#         difference = temperatures[i] - temperatures[i - 1]
#         print(f"Різниця температур за {i + 1}-й день: {difference}")

# Завдання 6
# Створіть застосунок банк. Є список з рахунками
# клієнтів.
# Користувач вибирає одну з команд
# ● Додати клієнта
# ● Видалити клієнта
# ● Поповнити рахунок
# ● Зняти кошти
# ● Вихід
# При додаванні клієнта, добавте рахунок в 0грн в
# кінець списку.
# В інших випадках запросіть ID(індекс) клієнта і якщо
# він вірний, то проведіть операцію

accounts = []

while True:
    print()
    print("1 - Додати клієнта")
    print("2 - Видалити клієнта")
    print("3 - Поповнити рахунок")
    print("4 - Зняти кошти")
    print("5 - Вихід")

    command = input("Оберіть команду: ")

    if command == "5":
        print("До побачення!")
        break

    if command == "1":
        accounts.append(0)
        print(f"Клієнта додано. Його ID: {len(accounts) - 1}")

    elif command in ("2", "3", "4"):
        client_id = int(input("Введіть ID клієнта: "))

        if client_id < 0 or client_id >= len(accounts):
            print("Невірний ID клієнта")
            continue

        if command == "2":
            accounts.pop(client_id)
            print("Клієнта видалено")

        elif command == "3":
            amount = float(input("Сума поповнення: "))
            accounts[client_id] += amount
            print(f"Баланс: {accounts[client_id]} грн")

        elif command == "4":
            amount = float(input("Сума зняття: "))
            if amount > accounts[client_id]:
                print("Недостатньо коштів")
            else:
                accounts[client_id] -= amount
                print(f"Баланс: {accounts[client_id]} грн")

    else:
        print("Невідома команда")

    print("Рахунки:", accounts)
