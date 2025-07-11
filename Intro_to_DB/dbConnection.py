import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="employee"
)


"""""
print(mydb.get_server_info())
mycursor = mydb.cursor()

#Update data in table 
sql = "UPDATE Employees SET FirstName = %s WHERE EmployeeID = %s"
val = ("Kwame",1)
mycursor.execute(sql, val)
mydb.commit()

"""

#Delete data from table
sql = "DELETE FROM EMPLOYEES WHERE EMPLOYEEID = %s"
val = (2,)
mycursor = mydb.cursor()
mycursor.execute(sql,val)
mydb.commit()