def lookup_key(dictionary, value):
    keys_list = [key for key, val in dictionary.items() if val == value]
    return keys_list

# Приклад використання:
sample_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
search_value = 1

result_keys = lookup_key(sample_dict, search_value)

if result_keys:
    print(f"Знайдені ключі за значенням {search_value}: {result_keys}")
else:
    print(f"Не знайдено жодного ключа за значенням {search_value}.")
