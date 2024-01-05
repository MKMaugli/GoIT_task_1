def real_len(input_str):
    control_chars = ['\n', '\f', '\r', '\t', '\v']
    result_str = ''.join(char for char in input_str if char not in control_chars)
    return len(result_str)

# Приклад виклику
string1 = 'Alex\nKdfe23\t\f\v.\r'
string2 = 'Al\nKdfe23\t\v.\r'

length1 = real_len(string1)
length2 = real_len(string2)

print(f'Length of string1 without control characters: {length1}')
print(f'Length of string2 without control characters: {length2}')
