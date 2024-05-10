import mysql.connector
import os
import datetime
import time
from mysql.connector import DataError
import random
import matplotlib.pyplot as plt

from SupervisorModel import Supervisor
from EmployeeModel import Employee
from SupplierModel import Supplier

DATABASE = "bakery_management"
SQL_USERNAME = "root"
SQL_PASSWORD = "anuRadha0315!"


class ModelDelegator:
    def __init__(self):
        self.con, self.cursor = self.createCursor()
        self.subModel = None
        self.empID = None
        self.heirarchy = None

    def createCursor(self):
        con = mysql.connector.connect(host="localhost", user = SQL_USERNAME,
                                    password = SQL_PASSWORD, database=DATABASE)
        cur = con.cursor()
        return con , cur

    def closeSQLConnection(self):
        self.cursor.close()
        self.con.close()
        

    def verifyUser(self, username, password):
        self.cursor.execute("SELECT SUPP_id, type_ FROM details as d inner join logins as l on d.SUPP_id=l.E_id where EM_username= '{}' and EM_password= '{}'".format( username, password))
        self.empID,self.heirarchy = self.cursor.fetchall()[0]
        verified = False
        if self.heirarchy == "Supervisor":
            self.subModel = Supervisor(self.cursor,self.empID, self.heirarchy)
            verified = True
        elif self.heirarchy == "Employee":
            self.subModel = Employee(self.cursor,self.empID, self.heirarchy)
            verified = True
        elif self.heirarchy == "Supplier":
            self.subModel = Supplier(self.cursor,self.empID, self.heirarchy)
            verified = True
        else:
            verified = False
        return verified

    def getTableValue(self,tableName):
        return self.subModel.getTableDetails(tableName)

    def querySalesGroupedByLocation(self):
        table = None
        # write a query to get sales grouped by location.
        self.cursor.execute("select count(D_id), postal_code from delivery group by postal_code")
        table = self.cursor.fetchall()
        try:
            if self.heirarchy == "Supervisor":
                # table = {"02115":1,"02116":2}
                temp_x = []
                temp_y = []
                for item in table:
                    temp_x.append(item[0])
                    temp_y.append(item[1])
                return (temp_x,temp_y)
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
        return (None, None)

    def queryProfitLossStatement(self):
        table = None
        self.cursor.execute("select B_name, (b_sellingprice-price) as profit from bakery group by B_name;")
        table = self.cursor.fetchall()
        try:
            if self.heirarchy == "Supervisor":
                # table = {"02115":1,"02116":2}
                temp_x = []
                temp_y = []
                for item in table:
                    temp_x.append(item[0])
                    temp_y.append(item[1])
                return (temp_x,temp_y)
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
        return (None, None)

    def addToCustomerTable(self,val1, val2, val3, val4):
        try:
            if self.heirarchy == "Supervisor":
                self.cursor.execute("INSERT INTO customer (C_id, C_name, C_phonenumber, C_lastname ) VALUES ('{}', '{}', '{}', '{}')".format(val1,val2,val3,val4))
                return True
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return False

    def addToDeliveryTable(self,val1, val2, val3, val4):
        try:
            if self.heirarchy == "Supervisor":
                self.cursor.execute("INSERT INTO delivery (D_id, D_address, postal_code, delivery_personscore ) VALUES ('{}', '{}', '{}', '{}')".format(val1,val2,val3,val4))
                return True
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return False


    def addToCustomerRequestTable(self,val1, val2, val3, val4):
        try:
            if self.heirarchy == "Supervisor":
                self.cursor.execute("INSERT INTO customer_request(CR_id, C_id, CR_request, CR_date ) VALUES ('{}', '{}', '{}', '{}')".format(val1,val2,val3,val4))
                return True
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return False


    def updateCustomerTable(self, val1, val2):
        try:
            if self.heirarchy == "Supervisor" or self.heirarchy == "Employee":
                self.cursor.execute("UPDATE customer set  C_name = '{}' where C_id= '{}';".format(val1, val2))
                return True
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return False


    def updateCustomerRequestTable(self, val1, val2):
        try:
            if self.heirarchy == "Supervisor" or self.heirarchy == "Employee":
                self.cursor.execute("UPDATE customer_request set  CR_request= '{}' where CR_id= '{}';".format(val1, val2))
                return True
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return False

    def queryDeliveryScore(self):
        try:
            if self.heirarchy == "Supervisor":
                self.cursor.execute("SELECT  D_id, deliveryboyLevel(delivery_personscore) FROM Delivery;")
                table = self.cursor.fetchall()
                return table
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return None

    def updateEmployeeName(self, val1, val2):
        try:
            if self.heirarchy == "Supervisor" or self.heirarchy == "Employee":
                self.cursor.execute("UPDATE employee SET E_lastname = '{}' WHERE E_id = '{}';".format(val1, val2))
                return True
            raise Exception("Access Denied")
        except Exception as e:
            print(e)
            return False
        


