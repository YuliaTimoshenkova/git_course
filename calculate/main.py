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
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print('%.2f + %.2f = %.2f' % (x, y, x + y))
            elif action == '-':
                print('%.2f - %.2f = %.2f' % (x, y, x - y))
            elif action == '*':
                print('%.2f * %.2f = %.2f' % (x, y, x * y))
            elif action == '/':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x / y))
                else:
                    print("Деление на ноль!")


if __name__ == "__main__":
    main()
