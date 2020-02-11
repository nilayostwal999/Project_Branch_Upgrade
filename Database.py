import sqlite3
import mysql.connector as myconnector

def updateRecord(enrollmentNumber,newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection):
      conn=sqlite3.connect("test.db")
      curobj=conn.cursor()
      curobj.execute("UPDATE student SET Branch=?,Roll3=?,Roll4=?,Roll5=?,Roll6=?,Roll7=?,Roll8=?,Section=? WHERE EnrollmentNumber=?",(newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection,enrollmentNumber))
      conn.commit()
      conn.close()

def updateData(enrollmentNumber,newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection):
      conn=myconnector.connect(host='localhost',database='test2',user='root',passwd='deepanshu')
      curobj=conn.cursor()
      query = ("update student set Branch='%s',Roll3='%s',Roll4='%s',Roll5='%s',Roll6='%s',Roll7='%s',Roll8='%s',Section='%d' WHERE EnrollmentNumber='%s'"%(newBranch,newRoll3,newRoll4,newRoll5,newRoll6,newRoll7,newRoll8,newsection,enrollmentNumber)
      curobj.execute(query)
      conn.commit()
      conn.close()
