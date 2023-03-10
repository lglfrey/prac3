import pyodbc
import os
import os.path
import time
import Order
import pathlib
from pathlib import Path

cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()
def User(userId):
    os.system('cls')
    for row in cursor.execute(f"select * from [User] inner join [Loyality] on [Loyality_ID] = [ID_Loyality] where [ID_User] = '{userId}'"):
         balance = row.Balance_User

    print(f"У вас на счету {balance} рублей.\n")
    try:
        function = int(input("Выберите функцию\n"
        "1 - Заказать блюдо\n"
        "2 - История покупок\n"
        "3 - Карта лояльности\n"
        "4 - Выйти из аккаунта\n"))
    except ValueError:
        print("Введены неверные данные")
        time.sleep(2)
        User(userId)

    if function > 0 and function <= 4:
        match function:
            case 1:
                Order.Order(userId)
            case 2:
                UserHistory(userId)
            case 3:
                UserLoyality(userId)
            case 4:
                os.system("python Main.py")
    else:
        print("Неправильная функция.")
        User(userId)

def UserHistory(userId):
    chequeId = []
    countFiles = 0
    for row in cursor.execute(f"select * from [Cheque] where [User_ID] = {userId}"):
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
        print("У вас еще нет истории. \n")
    time.sleep(1)
    User(userId)

def UserLoyality(userId):
    os.system('cls')
    for row in cursor.execute(f"select * from [User] inner join [Loyality] on [Loyality_ID] = [ID_Loyality] where [ID_User] = {userId}"):
        nameLoyality = row.Name_Loyality
        discountLoyality = row.Discount
        discount = discountLoyality * 100
    print(f"Ваша программа лояльности: {nameLoyality}, скидка: {discount}%\n")
    time.sleep(2)
    User(userId)