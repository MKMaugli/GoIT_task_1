def make_request(keys, values):
    # Перевірка на збіг довжин списків
    if len(keys) != len(values):
        return {}

    # Створення словника із відповідною відповідністю ключів та значень
    request_dict = dict(zip(keys, values))

    return request_dict

# Приклад використання:
keys = ["name", "age", "gender"]
values = ["John", 25, "Male"]

request = make_request(keys, values)
print(request)
