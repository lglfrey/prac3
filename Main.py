import os
import time
import phonenumbers
import maskpass
import Registration as Reg
import Authorization


def main():
    os.system('cls')
    os.listdir()
    print("Ресторан у Гаечки")
    try:
        enter = int(input("Выберите функцию: \n"
                          "1 - Регистрация\n"
                          "2 - Авторизация\n"
                          "3 - Выйти\n"))
        match enter:
            case 1:
                print("Регистрация\n")
                try:
                    inputPhone = int(input("Введите телефон\n+7"))
                except ValueError:
                    print("Неправильно введен номер телефона.")
                    time.sleep(2)
                    main()
                phone_number = "+7" + str(inputPhone)
                try_number = phonenumbers.parse(phone_number, "RU")
                if phonenumbers.is_valid_number(try_number):
                    if ("+" not in phone_number):
                        phone_number = "+" + phone_number
                else:
                    print("Неверно введен номер телефона.")
                    time.sleep(2)
                    main()
                password = maskpass.askpass(prompt="Введите пароль: \n", mask="*")
                Reg.Reg(phone_number, password)
                print("Регистрация прошла успешно!")
                time.sleep(2)
                main()
            case 2:
                print("Авторизация")
                phone_number = input("Введите телефон \n")
                password = maskpass.askpass(prompt="Введите пароль: \n", mask="*")
                Authorization.Auth(phone_number, password)
            case 3:
                print("До скорой встречи!\n")
                time.sleep(1)
                exit()
            case _:
                print("Выбрана неверная функция\n")
                time.sleep(1)
                main()
    except KeyboardInterrupt:
        print("Вы вышли из приложения. Всего хорошего!\n")
        exit()
    except ValueError:
        print("Неккоректный ввод")
        time.sleep(1)
        main()


main()
