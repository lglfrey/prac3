import pyodbc
import os
import os.path
import time
import Supply
import pathlib
from pathlib import Path
cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()

def admin(adminId):
    os.system('cls')
    for row in cursor.execute(f"select * from [Admin] where [ID_Admin] = '{adminId}'"):
         balance = row.Balance_Admin

    print("Добро пожаловать в админ панель!")
    print(f"У вас на счету {balance} рублей.\n")
    try:
        function = int(input("Выберите функцию\n"
        "1 - Заказать ингридиент\n"
        "2 - История покупок пользователей\n"
        "3 - Карты лояльности пользователей\n"
        "4 - Выйти из аккаунта\n"))
    except ValueError:
        print("Введены неверные данные")
        time.sleep(2)
        admin(adminId)
    except KeyboardInterrupt:
        print("Вы вышли из приложения!")
        exit()

    match function:
        case 1:
            Supply.suply(adminId)
        case 2:
            adminUsersHistory(adminId)
        case 3:
            adminUsersLoyality(adminId)
        case 4:
            os.system("python Main.py")
        case _:
            print("Выбрана неверная функция!")
            time.sleep(1)
            admin(adminId)

def adminUsersHistory(adminId):
    os.system('cls')
    userId, EmailUser, passwordUser, balanceUser, chequeId = [], [], [], []
    countFiles = 0
    for row in cursor.execute("select * from [User]"):
        userId.append(row.ID_User)
        EmailUser.append(row.Email_User)
        passwordUser.append(row.Password_User)
        balanceUser.append(row.Balance_User)
    print("Пользователи:\n")
    for i in range(len(EmailUser)):
        print(f"{i+1} - {EmailUser[i]} - {passwordUser[i]} - {balanceUser[i]}")
    
    try:
        idUser = int(input("Выберите пользователя для просмотра истории: \n"))
    except ValueError:
        print("Введены неверные данные")
        time.sleep(2)
        adminUsersHistory(adminId)

    if idUser > 0 and idUser <= len(userId) and userId.count(idUser) > 0:
        for row in cursor.execute(f"select * from [Cheque] where [User_ID] = {idUser}"):
            chequeId.append(row.ID_Cheque)
        for id in range(len(chequeId)):
            directory = Path(pathlib.Path.cwd(), 'Cheques', f'Cheque{chequeId[id]}.txt')
            if (os.path.exists(directory)):
                file = open(directory, 'r')
                strings = file.readlines()
                file.close()
                print("\n")
                for i in range(len(strings)):
                    print(strings[i])
                countFiles += 1
        if countFiles == 0:
            print("У пользователя еще нет истории. \n")
        quit = input("Выйти на главную: да/нет \n")
        if quit == "да":
            admin(adminId)
        elif quit == "нет":
            adminUsersHistory(adminId)
        else:
            print("Неверный ввод данных!")
            time.sleep(1)
            os.system('cls')
            adminUsersHistory(adminId)
    else:
        print("Неверное действие")
        time.sleep(2)
        adminUsersHistory(adminId)

def adminUsersLoyality(adminId):
    os.system('cls')
    EmailUser, passwordUser, balanceUser = [], [], []
    for row in cursor.execute("select * from [User]"):
        EmailUser.append(row.Email_User)
        passwordUser.append(row.Password_User)
        balanceUser.append(row.Balance_User)

    print("Пользователи:\n")
    for i in range(len(EmailUser)):
        print(f"{i+1} - {EmailUser[i]} - {passwordUser[i]} - {balanceUser[i]}")
    
    try:
        idUser = int(input("Выберите пользователя для просмотра карты лояльности: \n"))
    except ValueError:
        print("Введены неверные данные")
        time.sleep(2)
        adminUsersLoyality(adminId)

    if (idUser > 0 and idUser <= len(EmailUser)):
        for row in cursor.execute(f"select * from [User] inner join [Loyality] on [Loyality_ID] = [ID_Loyality] where [ID_User] = {idUser}"):
            nameLoyality = row.Name_Loyality
            discountLoyality = row.Discount
            discount = discountLoyality * 100
        print(f"Программа лояльности пользователя: {nameLoyality}, скидка: {discount}%\n")
        quit = input("Выйти на главную: да/нет \n")
        if quit == "да":
            admin(adminId)
        elif quit == "нет":
            adminUsersLoyality(adminId)
        else:
            print("Неверный ввод данных!")
            time.sleep(1)
            os.system('cls')
            adminUsersLoyality(adminId)
        
    else:
        print("Неверное действие.")
        time.sleep(2)
        adminUsersLoyality(adminId)