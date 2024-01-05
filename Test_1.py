import re

def replace_spam_words(text, spam_words):
    for spam_word in spam_words:
        pattern = re.compile(r'\b{}\b'.format(re.escape(spam_word)), flags=re.IGNORECASE)
        replacement = '*' * len(spam_word)
        text = pattern.sub(replacement, text)

    return text

# Приклад використання
spam_words = ['bad', 'word', 'spam']
text = "This is a bad Word, and it contains spam."
result = replace_spam_words(text, spam_words)
print(result)
