def game(list_of_lists, power):
    for sublist in list_of_lists:
        for value in sublist:
            if value <= power:
                power += value
            else:
                break

    return power

# Приклад використання:
example_list = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
initial_power = 1

result_energy = game(example_list, initial_power)
print(f"Загальна енергія гравця: {result_energy}")
