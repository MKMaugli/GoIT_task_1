def is_equal_string(utf8_string, utf16_string):
    # Декодування рядків у відповідних кодуваннях
    decoded_utf8 = utf8_string.decode('utf-8')
    decoded_utf16 = utf16_string.decode('utf-16')

    # Порівняння декодованих рядків
    return decoded_utf8 == decoded_utf16

# Приклад використання
utf8_str = b'This is a UTF-8 string'
utf16_str = b'\xff\xfeT\x00h\x00i\x00s\x00 \x00i\x00s\x00 \x00a\x00 \x00U\x00T\x00F\x00-\x008\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00\x00\x00'
result = is_equal_string(utf8_str, utf16_str)
print(result)
