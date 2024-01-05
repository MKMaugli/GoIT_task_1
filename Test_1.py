import sys

def parse_args():
    # Починаємо з індексу 1, щоб пропустити ім'я скрипта (перший аргумент)
    result = ' '.join(sys.argv[1:])
    return result

# Приклад виклику
args_string = parse_args()
print(args_string)
