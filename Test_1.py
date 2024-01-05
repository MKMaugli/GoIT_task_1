def is_spam_words(text, spam_words, space_around=False):
    # Зводимо весь текст до нижнього регістру
    normalized_text = text.lower()

    for spam_word in spam_words:
        # Зводимо слово до нижнього регістру
        normalized_spam_word = spam_word.lower()

        if space_around:
            # Шукаємо слово, яке повинно бути окремим в тексті
            if f" {normalized_spam_word} " in f" {normalized_text} ":
                return True
        else:
            # Шукаємо слово взагалі
            if normalized_spam_word in normalized_text:
                return True

    return False

# Приклади використання
print(is_spam_words("У діда в руках молоток.", ["лоток"]))  # True
print(is_spam_words("У діда в руках молоток.", ["лоток"], True))  # False

print(is_spam_words("У кота порожній лоток.", ["лоток"]))  # True
print(is_spam_words("У кота порожній лоток.", ["лоток"], True))  # True
