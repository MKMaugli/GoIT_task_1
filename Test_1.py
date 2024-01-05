def split_list(scores):
    if not scores:
        # Якщо список порожній, повертаємо два порожні списки.
        return [], []

    average_score = sum(scores) / len(scores)
    lower_half = [score for score in scores if score <= average_score]
    upper_half = [score for score in scores if score > average_score]

    return lower_half, upper_half

# Приклад використання:
student_scores = [75, 88, 92, 60, 78, 85, 95]
lower, upper = split_list(student_scores)

print("Нижня половина:", lower)
print("Верхня половина:", upper)
