import matplotlib.pyplot as plt

VIEW_MENU = [
    "Employee",
    "Make",
    "Sale Item",
    "Sales",
    "Supplier",
    "Product Request",
    "Bakery",
    "Purchase",
    "Sold To",
    "Customer",
    "Wants Delivery",
    "Delivery",
    "Requests",
    "Customer Requests"
]
    

class View:
    def __init__(self):
        print("Welcome to Bakery Management System")

    def printUsernameInput(self):
        print("Please enter the Username : ")
    
    def printPasswordInput(self):
        print("Please enter the Password : ")

    def printException(self, message):
        print(message)

    def printTable(self, table):
        print("The details are :  \n", table + "\n\n")

    def printLoggedInMessage(self):
        print("\nSuccessfully logged in \n" + "\n\n")

    def printFeaturesMenu(self):
        print("1.View Tables \n2.Edit Tables \n3.Additional Features\n\n")

    def printViewTableMenu(self):
        temp = ""
        for idx, item in enumerate(VIEW_MENU):
            temp = temp + str(idx+1) + ". " + "View " + str(item) + " Table \n\n"
        print(temp)

    def printTableDetails(self, table):
        # table = pd.DataFrame(table)
        if table:
            print(table)
            print("\n\n")

    def printAdditionalFeaturesMENU(self):
        print("\n\n1. Group Items sold by Postal code - bar chart \n\n2. Generate Profit Loss Statement per product \n\n3.Get delivery score \n\n")

    def printSalesChartByLocation(self, values):
        y,x = values
        plt.bar(x,y)
        plt.xlabel("Pincode")
        plt.ylabel("Sales Count")
        plt.show()

    def printProfitLossStatement(self, values):
        x,y = values
        plt.barh(x,y)
        plt.ylabel("Product name")
        plt.xlabel("Profit")
        plt.show()

    def printEditTableMenu(self):
        print("\n\n1.Add to Customer Table \n2.Add to delivery table \n3.Add to Customer request table \n4.Update Customer Table \n5.Update Customer Request Table \n 6.Update employee name trigger")

    def printSuccessMessage(self):
        print("\n\nAdded/Updated Successfully\n\n")

    def printSalesByEmployee(self, value):
        if value:
            print("The sales made by the abobe employee are, ", value, "\n\n")

    def printDeliveryScore(self, table):
        if table:
            print("\n\nThe delivery score table is\n\n")
            print(table)
            print("\n\n")
        
            
