def flatten(data):
    if not data:
        return []

    if isinstance(data[0], list):
        first_list = flatten(data[0])
        second_list = flatten(data[1:])
        return first_list + second_list

    return [data[0]] + flatten(data[1:])
