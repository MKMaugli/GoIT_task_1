import re

def find_all_words(text, word):
    pattern = re.compile(r'\b{}\b'.format(re.escape(word)), flags=re.IGNORECASE)
    matches = pattern.findall(text)

    return matches if matches else [word]

# Приклад використання
result = find_all_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', 'Python')
print(result)
