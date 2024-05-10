import pandas as pd
from AbstractModel import Abstract

accessDictionary = {
        "Employee" : False,
        "make" : True,
        "sale_item" : True,
        "sales" : True,
        "supplier" : False,
        "product_request" : True,
        "bakery" : True,
        "Purchase" : True,
        "sold_to" : True,
        "customer" : False,
        "wants_delivery" : True,
        "delivery" : True,
        "request" : True,
        "customer_requests" : True
    }

class Employee(Abstract):
    def __init__(self, cursor, empID, heirarchy):
        super().__init__()
        self.accessDictionary = accessDictionary
        self.empID = empID
        self.cursor = cursor
        self.heirarchy = heirarchy


    def getAccessDetails(self):
        return super().getAccessDetails()

    def getTableDetails(self, tableName):
        return super().getTableDetails(tableName)

    def isUpdateTable(self, tableName):
        return super().isUpdateTable(tableName)


if __name__ == "__main__":
    print("here")
    employee = Employee()
    print("access",employee.getAccessDetails())
    print("table",employee.getTableDetails("Employee"))

