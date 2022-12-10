# import required modules
import mysql.connector

# create connection object
mydb = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="cnpm_test")

# create cursor object
cursor = mydb.cursor()


def getAllHoKhau():
    query = "SELECT * FROM hokhau"
    cursor.execute(query)
    return cursor.fetchall()


def InsertTable(values):
    query = "INSERT INTO person (Relationship, FullName, OtherName,Birthday,Gender, RealAddress, CCCD, Ethnic, Nationality, JobAndOffice, CurrentAddress, CurrentDate, HOKHAU_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, values)
    mydb.commit()


def getData(hostId):
    query = "SELECT * FROM person WHERE HOKHAU_id = %s"
    val = (hostId,)
    cursor.execute(query, val)

    return cursor.fetchall()
