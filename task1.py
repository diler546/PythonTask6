def divide(number):
    return number % 3 == 0

number = int(input("Введите число:"))

if divide(number):
    print("Делится")
else:
    print("Не делится")