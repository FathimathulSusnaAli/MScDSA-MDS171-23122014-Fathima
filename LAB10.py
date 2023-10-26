class Students:
    def __init__(self):
        self.lis = {}


    def insert(self,Name,RollNo,Course,Marks1,Marks2,Marks3):
        temp = {"Roll No": RollNo,
                "Course":Course,
                "Subjects":{"English":Marks1,
                            "Maths":Marks2,
                            "Statistics":Marks3
                            }}
        
        self.lis[Name]=temp

    def edit(self,name,inputt):
        if inputt == "Details":
            valuess = input("Enter the Details which you would like to Edit: ")
            newValue = input("Enter the Editted Value: ")
            self.lis[name][valuess]=newValue
        elif inputt == "Marks":
            Subject = input("Enter the Subject Name to which you would to ")
            Marks = input("Enter the Marks to be Updated: ")
            self.lis[name]["Subjects"][Subject] = Marks
            print(self.lis)

        
    def deleteKey(self,keyy_value):
        del self.lis[keyy_value]
        print(self.lis)

    def display(self):
        print(self.lis)

    def Search(self,userinput):
        print(self.lis[userinput]) 

                
obj1= Students()

while True:
    print("1. Select this option to Insert the Values ")
    print("2. Select this option to Edit the Values ")
    print("3. Select this option to Delete the Values ")
    print("4. Select this option to Display the Values ")
    print("5. Select this option to Search for a Student ")


    choice = int(input("Enter the Choice 1/2/3/4/5: "))
    
    if choice == 1:
        Name = input("Enter the Student name: ")
        RollNo = input("Enter the Roll Number: ")
        Course = input("Enter the Course: ")
        Marks1 = input("Enter the Marks for English: ")
        Marks2 = input("Enter the Marks for Maths: ")
        Marks3 = input("Enter the Marks for Statistics: ")
        obj1.insert(Name,RollNo,Course,Marks1,Marks2,Marks3)

    elif choice == 2:
        name = input("Enter the Student Name")
        inputt = input("What would you like to edit? (Details/Marks)")
        obj1.edit(name,inputt)

    elif choice == 3: 
        key_value = input("Enter the Student Name to be Deleted: ")
        obj1.deleteKey(key_value)

    elif choice == 4:
        obj1.display()
    
    elif choice == 5:
        userinput = input("Enter the Student Name to be Searched up on: ")
        obj1.Search(userinput)
    

    else:
        print("Thank You For Your Co-operation!!!")
        exit()



        

                        
        

    