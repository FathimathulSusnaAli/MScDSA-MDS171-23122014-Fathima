# **LAB:07**
### **Concept Used**
##### **Menu Driven Restaurant**

##### The concept here is the list, dictioanry and iterating through them:

##### `1.` Define a function that create the orders and append them into a list, the created orders are of dictionary that consisted of unique orderid that is generated randomly.
##### `2.` With the orderid as the next key-value pair another item key is created that consisted of multiple key-value pairs in the list, this gets appended as per the user defined number of times that is given in the for loop with the range as shown below.
##### `3.` Once the order is created, the viewing and total billing is performed in another function that takes the order(mainlist) and iterates through that indexes the itemnumber with the main menu the multiplies the number of quantity with the item price mentioned in the list.




import random

Orders = []  #mainlist
Menu = [["Rice", 30], ["Biriyani", 120], ["Tea", 10], ["Coffee", 30]] #menu

def Create_Order():
    input_user_elts = int(input("Please Enter the Number of Items You Would Like to Order: "))    #for loop range, such that it gets appended
    order = {}
    count = 0
    r1 = random.randint(1, 9)
    r2 = random.randint(0, 9)
    r3 = random.randint(0, 9)
    r4 = random.randint(0, 9)
    r5 = random.randint(0, 9)
    orderid = str(r1) + str(r2) + str(r3) + str(r4) + str(r5)
    order["OrderId"] = orderid  #random number for orders is being generated

    order["Items"] = []
    
    for i in range(input_user_elts):
        print(Menu)
        Item_Number = input("Enter the Item Number from the provided list for Order Collection[Rice-0, Biriyani-1, Tea-2, Coffee-3]:\n ")
        Quantity_Number = input("Enter the Quantity for the Placed Item:\n ")
        order["Items"].append({"Item_Number": Item_Number, "Quantity": Quantity_Number})
    
    Orders.append(order)

def TotalBill():
    for order in Orders:
        total = 0
        count = 0
        for item in order['Items']:
            total += int(item["Quantity"])*Menu[int(item['Item_Number'])][1]
        print(order)
        print("*"*100)
        print("The Order provided is: ",Orders)
        print("The total Price for the Order is: \n",total)
        print("*"*100)
    

while True:
    print("*"*100)
    print("\nThe Restaurant Management\n")
    print("*"*100)
    print("1. Select this option to create a New Order\n")
    print("2. Select this option to View Orders\n")
    print("3. Select this option to Exit\n")
    print("*"*100)
    
    user_input = int(input("Enter the Option:"))
    
    if user_input == 1:
        print("*"*100)
        print("------------------------------------------The Menu Card--------------------------------------------\n\n",Menu,"\n")
        print("*"*100)
        Create_Order()
    elif user_input == 2:
        TotalBill()
    elif user_input == 3:
        exit()
    else:
        print("Please Enter a Valid Input!!!\n")

