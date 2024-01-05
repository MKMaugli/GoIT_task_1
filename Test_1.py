def get_recipe(path, search_id):
    # Відкриття файлу за вказаним шляхом у режимі 'r' за допомогою менеджера контексту with
    with open(path, 'r') as file:
        # Читання кожного рядка з файлу
        for line in file:
            # Розбиття рядка на складові частини за допомогою коми
            parts = line.strip().split(',')

            # Перевірка, чи search_id співпадає з першою частиною рядка (id)
            if parts[0] == search_id:
                # Створення словника із складових частин та повернення його
                recipe = {"id": parts[0], "name": parts[1], "ingredients": parts[2:]}
                return recipe

    # Якщо рецепта із зазначеним search_id у файлі немає, повернення None
    return None

# Приклад використання
file_path = "шлях_до_файлу.txt"
search_id = "60b90c3b13067a15887e1ae4"
recipe_info = get_recipe(file_path, search_id)
print(recipe_info)
