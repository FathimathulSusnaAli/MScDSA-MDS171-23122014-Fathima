namelist = []
search = input("Enter the Name to be searched: ")
def storeName(namelist):
    name = input("Enter the name to be saved")
    name = name.strip().title()
    namelist.append(name)    
    return name
def listName(namelist):
    print("*"*30)
    print("Names in the List")
    print("*"*30)
    print("*"*30)
    for name in namelist:
        print(name)
    print("*"*30)

def searchName(search,namelist):
    search = search.strip().title()
    found = False
    for i in namelist:
        if search == i:
            found = True
            print("The name searched is {}, present in the list,".format(search))
            break
    if found == True:
        print("The name exist in the list")
    else:
        print("Name doesnt exist")




print("*"*30)
print("Name Mangement System")
print("*"*30)  
while True:
    print("1. Enter a Name")
    print("2. List the Names")
    print("3. Search for a Name")
    print("4. Exit")
    choice = input("Enter Your Choice ")
    print("You have Entered choice: ",choice)
    if choice == "1":
        storeName(namelist)
    elif choice == "2":
        listName(namelist)
    elif choice == "3":
        searchName (search,namelist)
    elif choice == "4":
        break
    else:
        print("Invalid Opion Entered")

    
