import pyodbc
import os
import Admin
import User
import time

cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()
def Auth(phone, password):
    id_admin, id_user, phone_admin, pass_admin, phone_user, pass_admin = "", "", "", "", "", ""
    for row in cursor.execute(f"select * from [Admin] where [Phone_Admin] = '{phone}'"):
        phone_admin = row.Phone_Admin
        pass_admin = row.Password_Admin
        id_admin = row.ID_Admin
    for row in cursor.execute(f"select * from [User] where [Phone_User] = '{phone}'"):
        phone_user = row.Phone_User
        pass_user = row.Password_User
        id_user = row.ID_User
    try:
        if phone == phone_admin and password == pass_admin:
            Admin.admin(id_admin)
        elif phone == phone_user and password == pass_user:
            User.User(id_user)
        else:
            print("Введены неверные данные!")
            time.sleep(1)
            os.system("python Main.py")
    except ValueError:
        print("Были введены неверные данные!")
        time.sleep(1)
        os.system("python Main.py")