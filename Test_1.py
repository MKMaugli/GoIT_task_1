def data_preparation(list_data):
    merged_list = []

    for sublist in list_data:
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        merged_list.extend(sublist)

    return sorted(merged_list, reverse=True)

# Пример использования:
list_data = [[1, 2, 3], [3, 4], [5, 6]]
result = data_preparation(list_data)
print(result)
