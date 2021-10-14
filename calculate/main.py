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
              
                print('%.2f * %.2f = %.2f' % (x, y, x*y))

if __name__ == "__main__":
    main()
