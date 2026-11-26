print("Вітаємо вас у нашій піцерії")
print("Гарного вам дня!")

while True:
    print("=======Меню======\n 1. Вибрати піцу \n 2. Вихід \n ================")
    choice = input("Оберіть пункт меню: ")
    if choice == "1":
        name_pizza = input("Введіть назву піци: ")
        quantity = int(input("введіть колво піци: "))
        print(f"Замовлено {name_pizza}, {quantity} шт")
