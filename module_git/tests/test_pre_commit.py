while True:
    num = int(input("Введіть число від 1 до 9: "))

    if 1 <= num <= 9:
        for i in range(1, 11):
            print(f"{i} * {num} = {i * num}")
        break

    else:
        print("Помилка! Потрібно ввести число саме від 1 до 9. Спробуйте ще раз.")
