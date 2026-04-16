def lucky_ticket(ticket):
    halfticket = len(ticket) // 2

    sum1 = sum(map(int,ticket[:halfticket]))
    sum2 = sum(map(int,ticket[halfticket:]))

    return sum1 == sum2

ticket = input("Введите билет:")

if not ticket.isdigit():
    print("Введите только цифры")
elif len(ticket) % 2 !=0:
    print("Введите билет с четным количеством чисел")
else:
    if lucky_ticket(ticket):
        print("Билет счастливый")
    else:
        print("Билет не счастливый")



