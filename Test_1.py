def fibonacci(n):
    if n ==0:
        return 0
    elif n < 0:
        return print('Введено отрицательное число!')
    else:
        fib1 = fib2 = 1
        n = (int(n)-2)
        while n>0:
            fib1, fib2 = fib2, fib1 + fib2
            n -= 1
        return fib2
    
print(fibonacci(7))

#Эта же функция, но через рекурсию:
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
 
print(fibonacci_recursive(7))