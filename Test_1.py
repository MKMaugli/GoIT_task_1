def modeling(factor, *numbers, correction):
    result = 0
    for number in numbers:
        result += number * factor
    result = result - correction
    return result

print(modeling(10, 1, 2, 3, correction=2))  # 58

def modeling2(factor, *_, correction):
    factor = int(input('Enter number: '))
    result = factor*5 - correction
    return (result)
    
print(modeling2(10, correction=3))
