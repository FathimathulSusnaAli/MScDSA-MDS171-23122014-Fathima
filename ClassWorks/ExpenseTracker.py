#define a class expense tracker that stored the expenses
#and income in a dictionary
#implement the method to
#. store the transaction:
#. view transactions:
#. calculate the total expense/income.

#here we will be tracking the expenses dumps all of them into this dictionary. 

#approach :1
# expensetraker :{
#     "expense":[ ],
#     "income":[ ]
# }

#approach:2
#transaction = [{},{},{}]

class expensetracker():
    def __init__(self):

        self.transactions = {
            "Expenses" : [],
            "Income" :[]
        }

    def storetransaction(self,type,category,cost,desc,date):
        # type : expense / income
        # type: type/category
        # category: descriptions on the transactions
        # date [DD/MM/YYYY]

        transaction = {
            "Category":category,
            "Cost":cost,
            "Description":desc,
            "Date":date
        }
        if type == "Expenses":
            self.transactions["Expenses"].append(transaction)
        else: 
            self.transactions["Income"].append(transaction)
        return True
    def view_transactions(self):
        # print("INCOME")
        for expenses in self.transactions['Expenses']:
            print(expenses)
        # self.transactions
    def total_incomeexpense(self):
        print("Total Income")
        total_income = 0
        for income in self.transactions['Income']:
            total_income+=income["Cost"]
        print(total_income)
        
        print("Total Expenses")
        total_expense = 0
        for expenses in self.transactions['Expenses']:
            total_expense+=expenses["Cost"]
        print(total_expense)


    
expenseTracker = expensetracker()
ExpenseType = input("Please Enter the Type of Entry you would like to choose")
Category = input("Please Enter the type of Expenditure")
Cost = int(input("Enter the amount of Expenditure"))
Description = input("Enter the Descriptions: ")
Date = input("Enter the Date")
expenseTracker.storetransaction(ExpenseType.title(),Category,Cost,Description,Date)
expenseTracker.storetransaction("Income","Salary",60000,"Amazon","21/09/2023")
expenseTracker.storetransaction("Income","Pocket Money",10000,"Parents","29/10/2023")
expenseTracker.storetransaction("Income","Internship Salary",10000,"Google","30/10/2023")
expenseTracker.storetransaction("Expenses","Groceries",5000,"SUpermarket","30/10/2023")
expenseTracker.view_transactions()
# expenseTracker.total_incomeexpense()
# while True:
#     print("1.Enter the options to save the Expense/Income:")
#     print("2.Enter the Category you would like to choose:")
#     print("3.Please select this option to ")


