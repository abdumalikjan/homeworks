print("Привет, это бот для знакомства)")
sex = input('Введите ваш пол:')
if sex.lower() == "ж":
    age = int(input('Введите ваш возраст:'))
    if age >= 18:
        print("Супер")
        x = int(input())
        y = int(input())
        print(x-y)
        print(x+y)
        print(x/y)
        print(x*y)
    else:
        print('Вы не подходите')
else:
    print("Вы не девушка!")
