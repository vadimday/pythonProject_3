
input_string = input("Ряд: ")

if input_string == input_string[::-1]:

 print("Пал+")

else:

 print("Пал-")


text = input("Текст: ")

reserved_words = input("Слова через запятую: ").split(',')



for word in text.split():



 if word.lower() in reserved_words:

   text = text.replace(word, word.upper())



print(text)



text = input("Текст: ")



num_sentences = text.count('.') + text.count('!') + text.count('?')



print(f"Предложения в тексте: {num_sentences}")

