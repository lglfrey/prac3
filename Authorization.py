import pyodbc
import os
import Admin
import User
import time

cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()
def Auth(Email, password):
    id_admin, id_user, Email_admin, pass_admin, Email_user, pass_admin = "", "", "", "", "", ""
    for row in cursor.execute(f"select * from [Admin] where [Email_Admin] = '{Email}'"):
        Email_admin = row.Email_Admin
        pass_admin = row.Password_Admin
        id_admin = row.ID_Admin
    for row in cursor.execute(f"select * from [User] where [Email_User] = '{Email}'"):
        Email_user = row.Email_User
        pass_user = row.Password_User
        id_user = row.ID_User
    try:
        if Email == Email_admin and password == pass_admin:
            Admin.admin(id_admin)
        elif Email == Email_user and password == pass_user:
            User.User(id_user)
        else:
            print("Введены неверные данные!")
            time.sleep(1)
            os.system("python Main.py")
    except ValueError:
        print("Были введены неверные данные!")
        time.sleep(1)
        os.system("python Main.py")