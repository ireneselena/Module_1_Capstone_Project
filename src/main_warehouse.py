import mylib_warehouse as mylibw
import os
import sys
import csv

# Function to clear user's terminal screen when using the app
def clear_screen():
      # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Define different paths for each database 
PATH_WAREHOUSE = 'data/Warehouse_Inventory.csv'
PATH_SUPPLIER = 'data/Supplier_Information.csv'


def initialize_db():

    database1 = {} # Warehouse Inventory Database
    database2 = {} # Supplier Information Database

    # Initialize Warehouse Inventory Database
    with open(PATH_WAREHOUSE, 'r') as file1:
        # Create reader variable
        reader = csv.reader(file1, delimiter=";")
        # Initializing empty database
        database1 = {}
        # Updating data to database
        for row in reader:
            sku_id, name, stock, brand, category, supplier_id = row
            database1.update({sku_id: [sku_id, name, int(stock), brand, category, int(supplier_id)]})

    # Initialize Supplier Information Database
    with open(PATH_SUPPLIER, 'r')  as file2:
        # Create reader variable
        reader = csv.reader(file2, delimiter=';')
        # Initializing empty database
        database2 = {}
        # Updating data to database
        for row in reader:
            supplier_id, name, contact_person, email, country = row
            database2.update({int(supplier_id): [int(supplier_id), name, contact_person, email, country]})


    return database1, database2

# Main function
def main():

    menulist = '''
    Welcome to Our Warehouse Inventory System!
    
    Menu Selection:
    1. Show Warehouse Inventory
    2. Add Warehouse Inventory
    3. Show Stock Information
    4. Update Item Information Details
    5. Delete Item Inventory 
    6. Show Supplier Information
    7. Exit Program
    '''

    global database1, database2

    while True: 
        # Show main menu list to user
        print(menulist)

        # Ask user to input a number from main menu list
        option = mylibw.integer_validation("Please input option you want to select: ", minval = 1, maxval = 7)

        # Run function as the number inputted
        # Show Warehouse Inventory
        if option == 1:
            mylibw.show(database1)

        # Add Warehouse Inventory    
        elif option == 2:
            mylibw.add(database1, database2)

        # Show Stock Information
        elif option == 3:
            mylibw.stockInfo(database1)

        # Update Item Information Details
        elif option == 4:
            mylibw.updateInfo(database1)

        # Delete Item Inventory
        elif option == 5:
            mylibw.delete(database1)

        # Show Supplier Information Menu
        elif option == 6:
            mylibw.supplier(database1, database2)

        # Exit Program
        else:
            break

         # Keeping warehouse inventory database renewed
        with open(PATH_WAREHOUSE, 'w') as file1:
            # Creating 'writer' variable
            writer1 = csv.writer(file1, delimiter=";")
            # Writing data into csv file
            writer1.writerows(database1.values())

        # Keeping supplier information database renewed
        with open(PATH_SUPPLIER, 'w') as file2:
            # Creating 'writer' variable
            writer2 = csv.writer(file2, delimiter=";")
            # Writing data into csv file
            writer2.writerows(database2.values())


if __name__ == "__main__":
    # Clear user interface
    clear_screen()

     # Organizing database file location
    if getattr(sys, 'frozen', False):
        PATH_WAREHOUSE = sys._MEIPASS
        PATH_WAREHOUSE = os.path.join(PATH_WAREHOUSE, 'data/Warehouse_Inventory.csv')
        PATH_SUPPLIER = sys._MEIPASS
        PATH_SUPPLIER = os.path.join(PATH_SUPPLIER, 'data/Supplier_Information.csv')
    else:
        PATH_WAREHOUSE = os.getcwd()
        PATH_WAREHOUSE = os.path.join(PATH_WAREHOUSE, 'data/Warehouse_Inventory.csv') 
        PATH_SUPPLIER = os.getcwd()
        PATH_SUPPLIER = os.path.join(PATH_SUPPLIER, 'data/Supplier_Information.csv') 

    # Initializing databases
    database1, database2 = initialize_db()

    # Start main menu
    main()

