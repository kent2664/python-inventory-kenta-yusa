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
        return f"{self.product_id},{self.name},{self.brand},{self.category},{self.price},{self.quantity}"

FILE_NAME = "inventory_data.txt"

def save_inventory(inventory_dict):
    # Save the inventory dictionary to a text file.
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for product_obj in inventory_dict.values():
                # str(product_obj) automatically calls the __str__ method
                f.write(str(product_obj) + "\n")
        print("Inventory successfully saved.")
    except IOError as e:
        print(f"Error: Could not write to file. {e}")

def load_inventory():
    # Read stored inventory from the file and return it as a dictionary.
    inventory_dict = {}
    
    # Check if the file exists before attempting to open it
    if not os.path.exists(FILE_NAME):
        return inventory_dict  # Return an empty dictionary if file doesn't exist

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                # Remove newline characters and split by comma
                data = line.strip().split(',')
                if len(data) == 6:
                    p_id, name, brand, cat, price, qty = data
                    # Reconstruct the Product object and add it to the dictionary
                    product_obj = Product(p_id, name, brand, cat, price, qty)
                    inventory_dict[p_id] = product_obj
        print("Data successfully loaded from file.")
    except Exception as e:
        print(f"An error occurred while loading: {e}")
        
    return inventory_dict

inventory = load_inventory()
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
    save_inventory(inventory)
    print("Item added successfully!")

def viewInventory():
    print("Current Inventory:\n" + "-" * 25)
    all_info = "\n".join(str(p) for p in inventory.values())
    print(all_info)
    print("-" * 25)

def updateItem(itemName):
    target = None
    for item in inventory.values():
        if itemName == item.name:
            target = Product(item.product_id, itemName, item.brand, item.category, item.price, item.quantity)
    ## if it's not found, display error message
    if target is None:
        print("There is no items that match the name :(")
        return
    else :
        inventory[target.product_id].quantity = int(input("Enter new quantity: >"))
        save_inventory(inventory)
    print("Inventory updated successfully!")
def deleteItem(itemName):
    target = None
    for item in inventory.values():
        if itemName == item.name:
            target = Product(item.product_id, itemName, item.brand, item.category, item.price, item.quantity)
    ## if it's not found, display error message
    if target is None:
        print("There is no items that match the name :(")
        return
    else :
        removedProduct = inventory.pop(target.product_id)
        save_inventory(inventory)
    print(f"Delete procedure is successfly done! :{removedProduct}")
print("Welcome to the Inventory Management System!")
while(selectedOption != 5):
    printMenu(mainMenu)
    selectedOption = int(input("Select an option (1-5): > "))
    if(selectedOption not in range(1,6)):
        print("Invalid option. Please try again.")
        continue
    if(selectedOption == 1):
        addItem()
    elif(selectedOption == 2):
        viewInventory()
    elif(selectedOption == 3):
        selected_name = str(input("Enter product name to update: > "))
        updateItem(selected_name)
    elif(selectedOption == 4):
        selected_name = str(input("Enter product name to delete: > "))
        deleteItem(selected_name)
        print("Remove")
print("Bye bye :)")

