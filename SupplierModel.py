import pandas as pd
from AbstractModel import Abstract

accessDictionary = {
        "Employee" : False,
        "make" : False,
        "sale_item" : False,
        "sales" : False,
        "supplier" : False,
        "product_request" : True,
        "bakery" : False,
        "Purchase" : False,
        "sold_to" : False,
        "customer" : False,
        "wants_delivery" : False,
        "delivery" : False,
        "request" : False,
        "customer_requests" : False
    }
class Supplier(Abstract):
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
    employee = Supplier()
    print("access",employee.getAccessDetails())
    print("table",employee.getTableDetails("Raw Material"))
    print("table",employee.getTableDetails("Supplier"))


