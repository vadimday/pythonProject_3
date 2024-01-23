text = input("Текст: ")

reserved_words = input("Слова через запятую: ").split(",")

for word in reserved_words:

   text = text.replace(word.strip(), word.strip().upper())

print(" текст:")

print(text)