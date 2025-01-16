import mysql.connector
import pyodbc
from tkinter import messagebox, Tk

def save_data_mysql(name, age, sex, fbs, exag, chestpain, resting, stsegment, clas, bloodpressure, chl, maxheart, oldpeak):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",
            database="your_mysql_database"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO heart_attack (name, age, sex, fbs, exag, chestpain, resting, stsegment, clas, bloodpressure, chl, maxheart, oldpeak) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (name, age, sex, fbs, exag, chestpain, resting, stsegment, clas, bloodpressure, chl, maxheart, oldpeak)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Data saved to MySQL successfully")
    except Exception as e:
        messagebox.showerror("Database Error", f"MySQL error: {e}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def save_data_sqlserver(name, age, sex, fbs, exag, chestpain, resting, stsegment, clas, bloodpressure, chl, maxheart, oldpeak):
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=your_sql_server;'
            'DATABASE=your_sql_database;'
            'UID=your_username;'
            'PWD=your_password;'
        )
        cursor = conn.cursor()
        sql = "INSERT INTO heart_attack (name, age, sex, fbs, exag, chestpain, resting, stsegment, clas, bloodpressure, chl, maxheart, oldpeak) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        val = (name, age, sex, fbs, exag, chestpain, resting, stsegment, clas, bloodpressure, chl, maxheart, oldpeak)
        cursor.execute(sql, val)
        conn.commit()
        print("Data saved to SQL Server successfully")
    except Exception as e:
        messagebox.showerror("Database Error", f"SQL Server error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
