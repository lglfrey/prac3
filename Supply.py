import pyodbc
from os import system, name
import os.path
import time
import Admin
cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()
def suply(adminId):
    _ = system('cls')
    for row in cursor.execute(f"select * from [Admin] where [ID_Admin] = {adminId}"):
        balance = row.Balance_Admin

    print(f"У вас на счету {balance} рублей.\n")

    nameIngridient, costIngridient, typeIngridient, countIngridient = [], [], [], []
    for row in cursor.execute("select * from [Ingridient] inner join [Type_Ingridient] on [Type_ID] = [ID_Type]"):
        nameIngridient.append(row.Name_Ingridient)
        costIngridient.append(row.Cost_Ingridient)
        typeIngridient.append(row.Name_Type)
        countIngridient.append(row.Count_Ingridient)

    print("0 - Назад\n")

    for i in range(len(nameIngridient)):
        print(f"{i+1} - {typeIngridient[i]} - {nameIngridient[i]} - {countIngridient[i]} шт. - {costIngridient[i]} Рублей \n")
                        
    for count in range(len(nameIngridient)):
        countIngridients = count+1
    
    try:
        idIngridient = int(input("Выберите ингридиент для поставки: \n"))
    except ValueError:
        print("Введены неверные данные")
        time.sleep(2)
        suply(adminId)

    if (idIngridient > 0 and idIngridient <= countIngridients):
        try:
            count = int(input("Введите количество поставки: \n"))
        except ValueError:
            print("Введены неверные данные")
            time.sleep(2)
            suply(adminId)

        for row in cursor.execute(f"select * from [Ingridient] inner join [Type_Ingridient] on [Type_ID] = [ID_Type] where [ID_Ingridient] = {idIngridient}"):
            currentName = row.Name_Ingridient
            currentCount = row.Count_Ingridient
            currentCost = row.Cost_Ingridient
            currentType = row.Name_Type

        endCount = currentCount + count
        sum = count * currentCost

        confirm = input(f"Поставка {currentType} - {currentName} в количестве {count} шт. - {sum} Рублей\n"
                        "Подтвердить заказ?\n").lower()
        
        if confirm == "yes" or confirm == "да":
            balance -= sum
            if balance >= 0:
                cursor.execute(f"update [Admin] set [Balance_Admin] = {balance} where [ID_Admin] = {adminId}")
                cnxn.commit()
                print("Выполняется заказ...")
                cursor.execute(f"update [Ingridient] set [Count_Ingridient] = {endCount} where [ID_Ingridient] = {idIngridient}")
                cnxn.commit()
                
                time.sleep(2)
                print("Заказ выполнен!")
                suply(adminId)
            else:
                print("Недостаточно средств на счету.")
                time.sleep(2)
                suply(adminId)
        elif confirm == "no" or confirm == "нет":
            print("Отмена заказа...")
            time.sleep(2)
            suply(adminId)
        else:
            print("Неправильный ввод.")
            time.sleep(2)
            suply(adminId)
    elif idIngridient == 0:
        print("Выход на главную...")
        time.sleep(2)
        Admin.admin(adminId)
    else:
        print("Некорректные данные")
        time.sleep(2)
        suply(adminId)