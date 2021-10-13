import math

import mysum

def main():

    while True:
        
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            # x
            x = float(input("x = "))
            # y
            y = float(input("y = "))
            # lalal
            if action == '+':
                # dsdsa
                print('%.2f + %.2f = %.2f' % (x, y, x+y))
            # dsadas
            elif action == '-':
                # czxczx
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

if __name__ == "__main__":
    main()
