# Завдання 1
# Користувач вводить рядок англійською мовою. Порахуйте
# скільки в ньому голосних літер(aeuio)
# Виправіть помилки в коді


# text = input("Введіть рядок англійською мовою: ")
#
# count = 0
#
# for letter in text:
#     if letter in "aeiou":
#         count += 1
#
#
# print(f"Кількість голосних літер: {count}")

# Завдання 2
# Користувач вводить текст.
# Після чого запускається цикл і користувач вводить певне
# слово. Треба це слово в тексті замінити на верхній регістр.
# Цикл закінчується коли введено EXIT
# Приклад:
# Текст – a big red fox is eating red apple
# Слово red – a big RED fox is eating RED apple
# Слово fox – a big RED FOX is eating RED apple
# Слово EXIT – кінець програми, показати результат
#
# text = input("enter some text: ")
#
# for i in text:
#     word = input("enter some word: ")
#     new_word = text.replace(word, word.upper())
#     print(new_word)

# Завдання 3
# Користувач вводить текст. Порахуйте скільки в ньому речень

text = input("enter some text: ")

count = text.count(".") + text.count("!") + text.count("?")

print("Речень: ", count)
