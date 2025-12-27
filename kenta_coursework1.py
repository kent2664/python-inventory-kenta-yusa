mainMenu = ("1. Add Item","2. View Inventory ","3. Update Item", "4. Remove Item","5. Exit")

class Product:
    def __init__(self, product_id, name, brand, category, price, quantity):
        # Attributes
        self.product_id = product_id
        self.name = name
        self.brand = (brand, )
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        # display information
        return f"ID: {self.product_id} | Name: {self.name} | Brand: {self.brand} | Category: {self.category} Price: ${self.price} | Quantity: {self.quantity}"

inventory = dict()
used_ids = set()
categories = ["Electronics", "Home", "Office"]
selectedOption = 0
## display menu
def printMenu(menuItems):
    for item in menuItems:
        print(item)
## add items
def addItem():
    ## taking input data
    inputProduct = str(input("Enter product name: > "))
    inputCategory = str(input(f"Enter category {categories}: > "))
    if inputCategory not in categories:
        inputCategory = str(input(f"Enter category Again :( {categories}: > "))
    inputBrand = str(input("Enter brand name: > "))
    inputQuantity = int(input("Enter quantity: > "))
    inputPrice = float(input("Enter price: > "))

    ## generate new id and add id to set
    new_id = max(used_ids) + 1 if used_ids else 101
    used_ids.add(new_id)
    ## create instance
    product = Product(new_id ,inputProduct, inputBrand, inputCategory, inputQuantity, inputPrice)
    ## add inventory
    inventory[new_id] = product
    print("Item added successfully!")
    for item in inventory.values():
        print(item)
        print("-" * 20) # display item info
print("Welcome to the Inventory Management System!")
while(selectedOption != 5):
    printMenu(mainMenu)
    selectedOption = int(input("Select an option (1-5): > "))
    if(selectedOption not in range(1,6)):
        print("Invalid option. Please try again.")
        continue
    if(selectedOption == 1):
        addItem()
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

