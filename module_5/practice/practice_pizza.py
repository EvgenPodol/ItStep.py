print("Вітаємо вас у нашій піцерії")
print("Гарного вам дня!")

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
        print("Маргарита – 150 грн \n Пепероні – 180 грн \n Чотири сири – 200 грн")
        name_pizza = input("Введіть назву піци: ")
        if (
            name_pizza != "Маргарита"
            and name_pizza != "Пепероні"
            and name_pizza != "Чотири сири"
        ):
            print("Введено неправильну назву піци")
            continue
        quantity = int(input("Введіть кількість піци: "))
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
            print(f"Маргарита {margarita} {margarita * 150} грн")
            total = total + margarita * 150
        if pepperoni > 0:
            print(f"Пепероні {pepperoni} {pepperoni * 180} грн")
            total = total + pepperoni * 180
        if four_cheese > 0:
            print(f"Чотири сири {four_cheese} {four_cheese * 200} грн")
            total = total + four_cheese * 200
        print("--------------------------------------")
        print(f"Загальна вартість: {total} грн")
        print("======================================")
        print("Дякуємо за замовлення!")
    else:
        print("Невірний пункт меню")
