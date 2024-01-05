points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if not coordinates or len(coordinates) == 1:
        # Для порожнього списку або списку з однією координатою повертаємо 0.
        return 0

    points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}

    total_distance = 0
    for i in range(len(coordinates) - 1):
        point1, point2 = min(coordinates[i], coordinates[i + 1]), max(coordinates[i], coordinates[i + 1])
        total_distance += points.get((point1, point2), 0)

    return total_distance

# Приклад використання:
quad_coordinates = [0, 1, 3, 2, 0]

result_distance = calculate_distance(quad_coordinates)
print(f"Загальна відстань пролетіла дрон: {result_distance}")

    
    
        
    
    
    
        
        
        
            
        
            
        
    