
sum = 0
while True:
    num = int(input("Введіть число (0 для виходу): "))
    if num == 0:
        break
    for i in range(num + 1):
        sum = sum + i
    print(sum)
    
    