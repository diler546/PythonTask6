def divide(number):
    return 100 / number

try:
    number = int(input("Введите число:"))
    print(divide(number))
except ValueError:
    print("Введена строка")
except ZeroDivisionError:
    print("Деление на ноль")
