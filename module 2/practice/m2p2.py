# """Завдання 1"""
# # Задаємо наближене значення числа пі
# pi = 3.1415
#
# # Зчитуємо радіус від користувача та перетворюємо його на дробове число
# radius = float(input("Введіть радіус: "))
#
# # Обчислюємо площу круга за формулою S = π * r²
# area = pi * radius ** 2
#
# # Виводимо площу, округлену до двох знаків після коми
# print(f"Площа кола: {area:.2f}")
#
# """Завдання 2"""
# price = float(input("Введіть ціну однієї кружки: "))
# budget = float(input("Введіть бюджет: "))
# count = int(budget // price)
# remainder = count % price
# print(f"Можна купити: {count} кружок")
# print(f"Залишок грошей: {remainder}")
# """завдання 3"""
#
# meters = float(input("Введіть довжину в метрах: "))
# feet = meters * 3.2808399
# yards = meters * 1.0936133
# print(f"{meters} м = {feet:.2f} футів")
# print(f"{meters} м = {yards:.2f} ярдів")

# """Завдання 4"""
# price = float(input("Введіть ціну однієї кружки: "))
# budget = float(input("Введіть бюджет: "))
# count = int(budget // price)
# remainder = budget % price
# print(f"Можна купити: {count} кружок")
# print(f"Залишок грошей: {remainder}")

"""Завдання 5"""
#
# time = int(input("Введіть кількість хвилин:"))
# hours = time/60
# minutes = time%60
# print(f"Годин: {hours: .0f} \n Хвилин: {minutes: .0f} ")

# """Завдання 6"""
#
# apple = int(input("Введіть кількість яблук:"))
# milk = int(input("Введіть кількість молока (л):"))
# pies_apples = apple // 4
# pies_milk = int(milk // 1.2)
# pies = min(pies_apples, pies_milk)
# remaining_milk = milk - (pies_milk * 1.2)
# remaining_apples = apple - (pies_apples * 4)
# print("\n === рецепт пирога ===")
# print(f"Можна спекти пирогів: : {pies} \n "
#       f"Залишиться яблук: {remaining_apples} \n "
#       f"Залишиться молока: {remaining_milk: .2f}")
#
# #завдання 7
#
# diposit_amount = float(input("Введіть вашу суму вкладу:"))
# interest = int(input("введіть ваш відсоток ставки:"))
# multiplier = 1 + interest / 100
# year1 = diposit_amount * multiplier
# year2 = year1 * multiplier
# year3 = year2 * multiplier
# year4 = year3 * multiplier
# year5 = year4 * multiplier
# print(f"Через 1 рік: {year1:.2f}")
# print(f"Через 2 роки: {year2:.2f}")
# print(f"Через 3 роки: {year3:.2f}")
# print(f"Через 4 роки: {year4:.2f}")
# print(f"Через 5 років: {year5:.2f}")

#завдання 8
days = int(input("введіть колв днів:"))
year = days // 365
remaining_days = days % 365
week = remaining_days // 7
day = remaining_days % 7
print( f"{days} днів це:\n"
       f"\t {year} років\n"
       f"\t {week} тижнів\n"
       f"\t {day} днів")