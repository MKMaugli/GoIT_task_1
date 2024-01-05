def get_cats_info(path):
    cats_list = []

    # Відкриття файлу за вказаним шляхом у режимі 'r' за допомогою менеджера контексту with
    with open(path, 'r') as file:
        # Читання кожного рядка з файлу
        for line in file:
            # Розбиття рядка на складові частини за допомогою коми
            parts = line.strip().split(',')

            # Створення словника із складових частин та додавання його до списку
            cat_info = {"id": parts[0], "name": parts[1], "age": parts[2]}
            cats_list.append(cat_info)

    # Повернення списку котів
    return cats_list

# Приклад використання
file_path = "шлях_до_файлу.txt"
cats_info = get_cats_info(file_path)
print(cats_info)
