def encode(data):
    if not data:
        return []

    result = []
    for i in range(len(data)):
        if i + 1 == len(data):
            result.append(data[i])
            break

        if data[i] == data[i + 1]:
            result.append(data[i])
            result.append(len(data) - i - 1)
        else:
            result.append(data[i])

    return result

# Приклад використання:
data = "XXXXXZXYYYYZZ"

result = encode(data)
print(result)
