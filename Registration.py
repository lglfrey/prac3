import pyodbc
import os
import time
import random
cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()

def Reg(Email, password):
    os.system('cls')
    loyality = 1
    confirmReg = True
    Email_user, Email_admin = [], []
    for row in cursor.execute("select * from [User]"):
        Email_user.append(row.Email_User)
    
    for row in cursor.execute("select * from [Admin]"):
        Email_admin.append(row.Email_Admin)

    for id in range(len(Email_admin)):
        if Email == Email_admin[id]:
            confirmReg = False

    for id in range(len(Email_user)):
        if Email == Email_user[id]:
            confirmReg = False
    
    if confirmReg == True:
        random.seed()
        balance = random.randint(1000, 10000)
        cursor.execute("insert into [User] ([Loyality_ID], [Email_User], [Password_User], [Balance_User]) values (?, ?, ?, ?)", 
                    loyality, Email, password, balance)
        cnxn.commit()
        time.sleep(2)
        print("Аккаунт зарегистрирован.")
        time.sleep(2)
        os.system("python Main.py")

    else:
        print("Такой номер телефона уже зарегистрирован")
        time.sleep(2)
        os.system("python Main.py")