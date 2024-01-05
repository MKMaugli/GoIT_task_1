import re

def find_word(text, word):
    result = {'result': False, 'first_index': None, 'last_index': None, 'search_string': word, 'string': text}
    
    match = re.search(re.escape(word), text)

    if match:
        result['result'] = True
        result['first_index'] = match.start()
        result['last_index'] = match.end()
        result['search_string'] = text[result['first_index']:result['last_index']]

    return result

# Пример использования
result1 = find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python")

result2 = find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "python")

print(result1)
print(result2)
