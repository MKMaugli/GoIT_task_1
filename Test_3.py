def game(lists, power):
    for sublist in lists:
        for energy in sublist:
            if energy <= power:
                power += energy
            else:
                break

    return power

# Приклад використання:
example_list = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
initial_power = 1

result_energy = game(example_list, initial_power)
print(f"Загальна енергія гравця: {result_energy}")
