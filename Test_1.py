def capital_text(s):
    result = ""
    capitalize_next = True

    for char in s:
        if capitalize_next and char.isalpha():
            result += char.upper()
            capitalize_next = False
        else:
            result += char

        if char in ('.', '!', '?'):
            capitalize_next = True

    return result

# Приклад використання:
text = "hello world. how are you today? i hope you're doing well!"
result_text = capital_text(text)
print(result_text)
