import string
text = "123 ."
text = text.capitalize()
digits_count = sum(c.isdigit() for c in text)
punctuation_count = sum(c in string.punctuation for c in text)
exclamation_count = text.count('!')

print(f"Исправленный текст: {text}")

print(f"Количество цифр: {digits_count}")

print(f"Количество знаков препинания: {punctuation_count}")

print(f"Количество восклицательных знаков: {exclamation_count}")