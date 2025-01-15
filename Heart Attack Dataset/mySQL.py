import mysql.connector
from tkinter import messagebox

def SaveDataMySQL(name,age,sex,fbs,exag,chestpain,resting,stsegment,clas,bloodpressure,chl,maxheart,oldpeak):
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="1208200277")
        mycursor=mydb.cursor()
        print("connection established")
    except:
        messagebox.showerror("DataBase connection not established!")

SaveDataMySQL()

