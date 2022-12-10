# import required modules
import mysql.connector

# create connection object
mydb = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="cnpm_test")

# create cursor object
cursor = mydb.cursor()


def InsertTable(values):
    query = "INSERT INTO ho_khau (Relationship, FullName, OtherName,Birthday,Gender, RealAddress, CCCD, Ethnic, Nationality, JobAndOffice, CurrentAddress, CurrentDate) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, values)
    mydb.commit()


def getData():
    query = "SELECT * FROM ho_khau"
    cursor.execute(query)

    return cursor.fetchall()
