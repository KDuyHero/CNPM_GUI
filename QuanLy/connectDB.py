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

# thêm nhân khẩu


def InsertTable(values):
    query = "INSERT INTO person (Relationship, FullName, OtherName,Birthday,Gender, RealAddress, CCCD, Ethnic, Nationality, JobAndOffice, CurrentAddress, CurrentDate, HOKHAU_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, values)
    mydb.commit()

# sửa thông tin


def UpdateTable(values):
    query = "UPDATE person SET Relationship = %s, FullName =%s,OtherName=%s,Birthday=%s,Gender=%s, RealAddress=%s, CCCD=%s, Ethnic=%s, Nationality=%s, JobAndOffice=%s, CurrentAddress=%s, CurrentDate=%s WHERE CCCD =%s"
    cursor.execute(query, values)
    mydb.commit()


# xem chi tiết


def getPerson(CCCD):
    query = "SELECT * FROM person WHERE CCCD = %s"
    # biến truyền vào dưới dạng 1 mảng
    val = (CCCD,)
    cursor.execute(query, val)

    return cursor.fetchall()


def getHoKhau(hostId):
    query = "SELECT * FROM person WHERE HOKHAU_id = %s"
    val = (hostId,)
    cursor.execute(query, val)

    return cursor.fetchall()
