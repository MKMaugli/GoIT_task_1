sum = 0

while True:
    num = int(input("Введіть число (0 для виходу): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i%2 == 1:
            continue
        sum = sum + i
        print(sum)
    print(sum)
    
    