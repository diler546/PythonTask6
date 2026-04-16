def magic_date(data):
    datas = data.split('.')
    if int(datas[2][-2:]) == int(datas[0]) * int(datas[1]):
        return True
    else:
        return False

data = input("Введите дату(xx.xx.xxxx):")

if magic_date(data):
    print("Магическоя дата")
else:
    print("Обычная дата")