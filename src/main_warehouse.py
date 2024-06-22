import mylib_warehouse as mylibw
import os
import sys
import csv


def clear_screen():
      # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')


def initialize_db():
    with open(PATH, 'r') as file:
        # Membuat objek reader
        reader = csv.reader(file, delimiter=";")
        # Initializing empty database
        database = {}
        # Updating data to database
        for row in reader:
            sku_id, name, stock, brand, category = row
            database.update({sku_id: [sku_id, name, int(stock), brand, category]})

    return database


def main():

    menulist = '''
    Welcome to Our Warehouse Inventory System!
    
    Menu Selection:
    1. Show Warehouse Inventory
    2. Add Warehouse Inventory
    3. Show Stock Information
    4. Update Item Information Details
    5. Delete Item Inventory 
    6. Exit Program
    '''

    global database

    while True: 
        # Show main menu list to user
        print(menulist)

        # Ask user to input a number from main menu list
        option = mylibw.integer_validation("Please input option you want to select: ", minval = 1, maxval = 6)

        # Display function as the number inputted
        if option == 1:
            mylibw.show(database)
            
        elif option == 2:
            mylibw.add(database)

        elif option == 3:
            mylibw.stockInfo(database)

        elif option == 4:
            mylibw.updateInfo(database)

        elif option == 5:
            mylibw.delete(database)

        else:
            break


         # Keeping database renewed
        with open(PATH, 'w') as file:
            # Creating 'writer' variable
            writer = csv.writer(file, delimiter=";")
            # Writing data into csv file
            writer.writerows(database.values())

if __name__ == "__main__":
    # Clear user interface
    clear_screen()

     # Organizing database file location
    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/Warehouse_Inventory.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/Warehouse_Inventory.csv') 

    # Initializing database
    database = initialize_db()

    # Start main menu
    main()

