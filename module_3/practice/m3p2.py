# Завдання 1
# Користувач вводить свій вік, якщо він працездатного
# віку(18-65) то виведіть фразу «Працездатний/на», інакше
# years_old = int(input("Введіть ваш вік:"))
# if 18 <= years_old <= 65:
#     print("Працездатний/на")
# else:
#     print("Непрацездатний/на")

# Завдання 2
# До завдання 2 з попереднього заняття добавте додаткову
# перевірку: щоб отримати доступ користувач повинен ще й
# ввести правильний логін secret_login = "AliBaba"
# years_old = int(input("Введіть ваш вік:"))
# user_login = input("Введіть ваш логін:")
# secret_login = "AliBaba"
# if 18 <= years_old <= 65 and user_login == secret_login:
#     print("Працездатний/на")
# else:
#     print("Непрацездатний/на")

# Завдання 3
# Оформіть чек покупки. Користувач вводить ціну за
# одиницю товару, кількість товару та свій вік.
# Якщо користувач неповнолітній або старший за 65
# років, то застосуйте знижку 15%
# price = float(input("Введіть суму товару:"))
# quantity = int(input("Введіть кількість товару:"))
# age = int(input("Введіть ваш вік:"))
# if age == 18 or age >= 65:
#     all_price = price * quantity
#     discount = all_price * 0.85
#     print(f"Ви отримали знижку! До сплати: {discount}")
# else:
#     all_price = price * quantity
#     print(f"Ваш чек: {all_price}")

# Завдання 4
# Орендувати авто можна лише якщо
# ● у вас є ліцензія
# ● ви повнолітні
# ● ви не потрапляли в дтп
# Оцініть якість написаного коду, спробуйте його
# спростити використавши and\or
# age = int(input("Введіть ваш вік: "))
# license = input("Введіть чи є у вас ліцензія? так/ні: ")
# accident = int(input("Кількість дтп: "))
# if age >= 18 and license == "так" and accident == 0:
#     print("Оренда дозволена")
# else:
#     print("Оренда заборонена")

# Завдання 5
# В службі доставки діє акційна пропозиція, чи дорожча
# покупка тим більша знижка на доставку
# Ціна покупки Знижка на доставку
# < 500 грн повна ціна
# 500-1000 -5%
# 1000-2000 -20%
# >2000 доставка безкоштовно
# Напишіть програму яка запитує у користувача ціну
# покупки та виводить загальну вартість(покупки + доставка)
# Базова ціна доставки: 120 грн
# Знижка діє лише на доставку
# delivery = 120
# discount5 = 0.05
# discount20 = 0.20
# price = float(input("Введіть ціну: "))
# if price < 500:
#     allprice = price + delivery
#     print(f"Ваш чек: {allprice}")
# elif price >= 500 and price <= 1000:
#     delivery_discount = delivery - (delivery * discount5)
#     allprice = price + delivery_discount
#     print(f"Ваш чек: {allprice}")
# elif price >= 1000 and price <= 2000:
#     delivery_discount = delivery - (delivery * discount20)
#     allprice = price + delivery_discount
#     print(f"Ваш чек: {allprice}")
# elif price > 2000:
#     delivery_discount = 0
#     allprice = price + delivery_discount
#     print(f"Ваш чек: {allprice}")
