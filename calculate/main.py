import math

import mysum

def main():

    while True:
        
        # Выводим сообщение какие действия есть
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Факторизовать: @\n"
              "Выйти: q\n")
        # Переменная для хранения действия
        action = input("Действие: ")
        # Если action равен q то
        if action == "q":
            # Выводим сообщение
            print("Выход из программы")
            # Выходим из цикла
            break
        # Если action равен +, -, *, /, то
        if action in ('+', '-', '*', '/'):
            # Присваиваем значение переменной x
            x = float(input("x = "))
            # Присваиваем значение переменной y
            y = float(input("y = "))
            # Если action равен + то
            if action == '+':
                # Выводим сумму x и y
                print('%.2f + %.2f = %.2f' % (x, y, x+y))
            # Если action равен - то
            elif action == '-':
                # Выводим разность x и y
                print('%.2f - %.2f = %.2f' % (x, y, x-y))
            # Если action равен * то
            elif action == '*':
                # Выводим результат умножения x на y
                print('%.2f * %.2f = %.2f' % (x, y, x*y))
            # Если action равен / то
            elif action == '/':
                # Если y не равен нулю то
                if y != 0:
                    # Выводим результат деления x на y
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else: # Иначе
                    # Выводим сообщение, что на ноль делить нельзя
                    print("Деление на ноль!")
        if action == '@':
            x = int(input('Введите натуральный x = '))
            factors = []
            while x > 1:
                for i in range(2, x + 1):
                    if x % i == 0:
                        x = round(x / i)
                        factors.append(i)
                        break
            for factor in factors:
                print(factor)

if __name__ == "__main__":
    main()
