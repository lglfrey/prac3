import pyodbc
from os import system, name
import os.path
import time
import Order
import random
import datetime

cnxn = pyodbc.connect('Driver={SQL Server};Server=OLP\TEST;Database=Restaurant;Trusted_Connection=yes;')
cursor = cnxn.cursor()
now = datetime.datetime.now()

def ChequeSumUpd(userId, currentIdCheque, endIdLasagna):
    sum = 100
    ingridientId = []
    for row in cursor.execute(f"select * from [Lasagna_Ingridient] where [Lasagna_ID] = {endIdLasagna}"):
        ingridientId.append(row.Ingridient_ID)
    
    for id in range(len(ingridientId)):
        for row in cursor.execute(f"select * from [Ingridient] where [ID_Ingridient] = {ingridientId[id]}"):
            costIngridient = row.Cost_Ingridient
        sum += costIngridient

    cursor.execute(f"update [Cheque] set [Sum_Order] = {sum} where [ID_Cheque] = {currentIdCheque}")
    cnxn.commit()


def Cheque(userId, count):
    for row in cursor.execute("select * from [Lasagna]"):
        cost = row.Cost_Lasagna
    sum = count * cost
    currentTime = now.strftime("%d-%m-%Y %H:%M")
    random.seed()
    if random.randint(1, 10) > 5:
        ear = 1
    else:
        ear = 0
    cursor.execute(f"insert into [Cheque] ([User_ID], [Count_Lasagna], [Cost_Lasagna], [Sum_Order], [Time_Order], [Ear]) values (?, ?, ?, ?, ?, ?)", 
                   (userId, count, cost, sum, currentTime, ear))
    cnxn.commit()

def DropCheque(userId, currentIdCheque):
    hachapuries = []
    for row in cursor.execute(f"select * from [Cheque_Lasagna] where [Cheque_ID] = {currentIdCheque}"):
        hachapuries.append(row.Lasagna_ID)
    for id in range(len(hachapuries)):
        cursor.execute(f"delete [Lasagna] where [ID_Lasagna] = {hachapuries[id]}")
        cnxn.commit()
    cursor.execute(f"delete [Cheque] where [ID_Cheque] = {currentIdCheque}")
    cnxn.commit()
    
    time.sleep(2)
    Order.Order(userId)