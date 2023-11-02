def first(size, *args):
    return size + len(args)

# Пример вызова функции:
result = first(5, "first", "second", "third")
print(result)  # Выведет число: 8 (5 + 3)

def second(size, **args):
    return size + len(args)

second(3, comment_one="first", comment_two="second", comment_third="third")

result = second(3, comment_one="first", comment_two="second", comment_third="third")
print(result)
