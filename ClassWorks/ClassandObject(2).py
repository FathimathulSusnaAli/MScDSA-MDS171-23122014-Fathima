# class Student:
#     #data members
#     #Name,email,phone,...

#     #member functions, for initializing the data memebers in the respective class.
#     # here __init__ play as a contructor(To Learn).


#     def __init__(self):
#         self.Name = "Abith"
#         self.email = "abith@gmail.com"
#         self.phone = 9456289632

#     def printStudent(self):   #just for printing purpose.
#         print("\nName: {}\n Email: {}\n Phone Number:{}\n".format(self.Name, self.email,self.phone))
        

#     def __str__(self):
#         pass

# abith = Student()
# abith.printStudent()
# print(abith.Name)


# Question 1

# class Student:
#     def __init__(self,a,b) :
#         self.name = a
#         self.stu_class = b

#     def __str__(self):
#         return self.name

# abc = Student("Fathima","MSC")
# print(abc.name,abc.stu_class)
# print (abc)
# print(type(abc))


# Create a class restaurant that accepts itemname and quantity as input
# inside you class you are having the item and its price as a dictioanry
# create a function calculate cost that prints the itemname, qty and price.

class Restaurant():
    def __init__(self, item_name,quantity):
        self.item_name = item_name
        self.quantity = quantity
        self.menu = {"rice":30,"chicken":100}

# dict = {}
def findCost(self):
    total = 0
    total = self.qty * self.menu[self.item]
    print(self.item_name,self.qty,total)


order = Restaurant("rice",4)
order.findCost()        






