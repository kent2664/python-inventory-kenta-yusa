mainMenu = ("1. Add Item","2. View Inventory ","3. Update Item", "4. Remove Item","5. Exit")

inventory = dict()
selectedOption = 0
def printMenu(menuItems):
    for item in menuItems:
        print(item)
print("Welcome to the Inventory Management System!")
while(selectedOption != 5):
    printMenu(mainMenu)
    selectedOption = int(input("Select an option (1-5): "))
    if(selectedOption not in range(1,6)):
        print("Invalid option. Please try again.")
        continue
    if(selectedOption == 1):
        # addContact()
        print("add")
    elif(selectedOption == 2):
        # searchContact()
        print("viewe")
    elif(selectedOption == 3):
        # removeContact()
        print("Update")
    elif(selectedOption == 4):
        # showAll()
        print("Remove")
print("Bye bye :)")