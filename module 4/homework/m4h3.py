pillow = 0
blanket = 0
lamp = 0
keychain = 0

print("1. Додати товар")
print("2. Видалити товар")
print("3. Очистити кошик")
print("4. Показати вміст кошика та суму")
print("5. Вихід")

while True:
    action = input("Оберіть номер дії: ")

    if action == "1" or action == "2":
        print("Товари:")
        print("подушка - 650 грн")
        print("ковдра - 1700 грн")
        print("лампа - 500 грн")
        print("брелок - 60 грн")
        print()
        name = input("Назва товару: ")
        if name not in ["подушка", "ковдра", "лампа", "брелок"]:
            print("Такого товару немає")
            continue

        qty_text = input("Кількість: ")
        if not qty_text.isdigit() or int(qty_text) == 0:
            print("Кількість має бути додатним цілим числом")
            continue
        qty = int(qty_text)

        if action == "1":
            if name == "подушка":
                pillow += qty
            elif name == "ковдра":
                blanket += qty
            elif name == "лампа":
                lamp += qty
            else:
                keychain += qty
            print("Товар додано")
        else:
            if name == "подушка" and qty <= pillow:
                pillow -= qty
            elif name == "ковдра" and qty <= blanket:
                blanket -= qty
            elif name == "лампа" and qty <= lamp:
                lamp -= qty
            elif name == "брелок" and qty <= keychain:
                keychain -= qty
            else:
                print("У кошику немає стільки цього товару")
                continue
            print("Товар видалено")

    elif action == "3":
        pillow = 0
        blanket = 0
        lamp = 0
        keychain = 0
        print("Кошик очищено")

    elif action == "4":
        total = pillow * 650 + blanket * 1700 + lamp * 500 + keychain * 60
        if total == 0:
            print("Кошик порожній")
        else:
            if pillow > 0:
                print(f"подушка: {pillow} шт.")
            if blanket > 0:
                print(f"ковдра: {blanket} шт.")
            if lamp > 0:
                print(f"лампа: {lamp} шт.")
            if keychain > 0:
                print(f"брелок: {keychain} шт.")
            print(f"Сума покупки: {total} грн")

    elif action == "5":
        print("До побачення!")
        break

    else:
        print("Такої дії немає")