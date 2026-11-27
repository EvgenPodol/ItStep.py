# Завдання 1
# Користувач вводить слово та індекс. Замініть символ під
# цим індексом на *. Скористайтесь зрізами
# Приклади:
# hello 1 – h*llo
# hello 2 – he*lo

# text = input("enter some text: ")
# index = int(input("enter index: "))
#
# if 0 <= index < len(text):
#     new_text = text[:index] + "*" + text[index + 1 :]
#     print(new_text)
# else:
#     print("Ошибка: такого индекса нет в строке.")

# Завдання 2
# Користувач вводить слово. Зробіть першу та останню
# літеру великою. Виправіть помилку в коді

# word = input("Введіть слово: ")
#
# result = word[0].upper() + word[1:-1] + word[-1].upper()
#
# print(result)

# Завдання 3
# Користувач вводить слова, поки не введе END. Виведіть в
# кінці ті слова, які починаються і закінчуються на одну і ту
# саму літеру(регістр не важливий).
# Приклади: око, дід, Ротор, Ангора

# matched_words = []
#
# while True:
#     word = input("Enter a word: ")
#     if word == "" or word == " ":
#         continue
#     if word.lower() == "end":
#         print(matched_words)
#         break
#     if word[0].lower() == word[-1].lower():
#         matched_words.append(word)
