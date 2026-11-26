print("Вітаємо вас у нашій піцерії")
print("Гарного вам дня!")

price_margarita = 150
price_pepperoni = 180
price_four_cheese = 200
max_pizzas = 15

margarita = 0
pepperoni = 0
four_cheese = 0

while True:
    print(
        "=======Меню======\n 1. Вибрати піцу \n 2. Вихід \n 3. Показати замовлення \n ================"
    )
    choice = input("Оберіть пункт меню: ")
    if choice == "1":
        print("Меню з цінами піц")
        print(
            f"Маргарита – {price_margarita} грн \n Пепероні – {price_pepperoni} грн \n Чотири сири – {price_four_cheese} грн"
        )
        name_pizza = input("Введіть назву піци: ")
        if name_pizza not in ["Маргарита", "Пепероні", "Чотири сири"]:
            print("Введено неправильну назву піци")
            continue

        quantity = int(input("Введіть кількість піци: "))
        if quantity <= 0:
            print("Кількість піц має бути більшою за 0")
            continue

        all_pizzas = margarita + pepperoni + four_cheese
        if all_pizzas + quantity > max_pizzas:
            print(f"В замовленні не може бути більше {max_pizzas} піц")
            print(f"Ви ще можете додати: {max_pizzas - all_pizzas} шт")
            continue

        if name_pizza == "Маргарита":
            margarita = margarita + quantity
        elif name_pizza == "Пепероні":
            pepperoni = pepperoni + quantity
        else:
            four_cheese = four_cheese + quantity
        print(f"Замовлено {name_pizza}, {quantity} шт")
    elif choice == "2":
        break
    elif choice == "3":
        total = 0
        print("========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print("Піца Кількість Вартість")
        print("--------------------------------------")
        if margarita > 0:
            print(f"Маргарита {margarita} {margarita * price_margarita} грн")
            total = total + margarita * price_margarita
        if pepperoni > 0:
            print(f"Пепероні {pepperoni} {pepperoni * price_pepperoni} грн")
            total = total + pepperoni * price_pepperoni
        if four_cheese > 0:
            print(f"Чотири сири {four_cheese} {four_cheese * price_four_cheese} грн")
            total = total + four_cheese * price_four_cheese
        print("--------------------------------------")
        print(f"Загальна вартість: {total} грн")
        print("======================================")
        print("Дякуємо за замовлення!")
    else:
        print("Невірний пункт меню")
