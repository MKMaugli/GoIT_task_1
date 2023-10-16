# num1 = int(input("Enter a number: "))
num1 = input("Enter a number: ")
num = float(num1)

try:
    num = float(num1)
    if num.is_integer():
        num = int(num)
    else:
        print("The number should be an integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if num >0:
    if (num %2) == 0:
        result = "Positive odd number"      #Положительное четное число
    else:
        result = "Positive even number"     #Положительное нечетное число
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print (result)

# print (height)
# print (is_active)