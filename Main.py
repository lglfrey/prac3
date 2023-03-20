import os
import time
import phonenumbers
import maskpass
import Registration as Reg
import Authorization
import random
import smtplib as smtp


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
                email = input("Введите почту\n")
                
                if (not ("@" and ".") in email):
                    print("Неверно введена почта.")
                    time.sleep(2)
                    main()
                password = maskpass.askpass(prompt="Введите пароль: \n", mask="*")

                smtpEmail = "test_test23r43@mail.ru"
                code = random.randint(100,999)
                smptObj = smtp.SMTP("smtp.mail.ru", 587)
                smptObj.starttls()
                smptObj.login(smtpEmail, "m7x9NpBJaHR7mm12Hntu")
                smptObj.sendmail(smtpEmail, email, f"Your code {code}")
                smptObj.quit()

                try:
                    confirmCode = int(input("Вам на почту выслан код подтверждения.\n"
                      "Введите его\n"))
                except ValueError:
                    print("Введены неверные данные")
                    time.sleep(2)
                    main()

                if code == confirmCode:
                    Reg.Reg(email, password)
                    print("Регистрация прошла успешно!")
                    time.sleep(2)
                    main()
                else:
                    print("Неверно введеный код!")
                    time.sleep(1)
                    main()
            case 2:
                print("Авторизация")
                email = input("Введите почту \n")
                password = maskpass.askpass(prompt="Введите пароль: \n", mask="*")

                smtpEmail = "test_test23r43@mail.ru"
                code = random.randint(100,999)
                smptObj = smtp.SMTP("smtp.mail.ru", 587)
                smptObj.starttls()
                smptObj.login(smtpEmail, "m7x9NpBJaHR7mm12Hntu")
                smptObj.sendmail(smtpEmail, email, f"Your code {code}")
                smptObj.quit()

                try:
                    confirmCode = int(input("Вам на почту выслан код подтверждения.\n"
                      "Введите его\n"))
                except ValueError:
                    print("Введены неверные данные")
                    time.sleep(2)
                    main()

                if code == confirmCode:
                    Authorization.Auth(email, password)
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