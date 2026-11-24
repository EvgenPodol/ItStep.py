print("Вітаємо вас у нашій бібліотеці")
print("Гарного вам дня")

# Завдання 14
# У файлі module_git/src/library.py реалізуйте програму
# роботи бібліотеки. Виконайте завдання в декілька кроків та
# збережіть відповідними комітами

while True:
    print("1. Отримати книжку")
    print("2. Вихід")
    print("3. Повернути книжку")
    choice = input("Оберіть пункт меню: ")
    name = input("Введіть ваше ім'я: ").strip()
    book = input("Введіть назву книги: ").strip()

    if choice == "1":
        if not name:
            print("Ім'я не може бути порожнім")
            continue
        if not book:
            print("Назва книжки не може бути порожнім")
            continue
        time = int(input("Введіть на скільки днів хочете взяти книгу:  "))
        if time < 0:
            print("кількість днів не може бути від’ємною")
            continue
        if time > 30:
            print("Забагато часу, максимум 30 днів!")

        print(f"Книжку {book} видано читачеві {name} на {time} днів")
    elif choice == "2":
        print("до побачення")
        break
    elif choice == "3":
        if not name:
            print("Ім'я не може бути порожнім")
            continue
        if not book:
            print("Назва книжки не може бути порожнім")
            continue
        print(f"Читач {name} повернув книжку {book}")
    else:
        print("Невірний вибір, спробуйте ще раз")
