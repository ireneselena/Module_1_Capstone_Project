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
        # Inisialisasi database kosong
        database = {}
        # Mengisi data ke dalam database
        for row in reader:
            sku_id, name, stock, brand, category = row
            database.update({sku_id: [sku_id, name, int(stock), brand, category]})

    return database


# List of inventory data in dictionary form where values = SKU id, item name, current stock, brand, category
# inventoryData = {
#     "HI01" : ['HI01', "White Paint", 50, "Nippon", "Home Improvement"],
#     "M01" : ["M01", "Wooden Plank", 100, "Lumber", "Materials"],
#     "T01": ["T01", "Electric Drill", 75, "Krisbow", "Tools"]
# }


def main():

    menulist = '''
    Welcome to Our Warehouse Inventory System!
    
    Menu Selection:
    1. Show Warehouse Inventory
    2. Add Warehouse Inventory
    3. Update Item Information Details
    4. Delete Item Inventory 
    5. Exit Program
    '''

    global database

    while True: 
        # Show main menu list to user
        print(menulist)

        # Ask user to input a number from main menu list
        option = mylibw.integer_validation("Please input option you want to select: ", minval = 1, maxval = 5)

        # Display function as the number inputted
        if option == 1:
            mylibw.show(database)
            
        elif option == 2:
                mylibw.add(database)

        elif option == 3:
            mylibw.updateInfo(database)

        elif option == 4:
            mylibw.delete(database)

        else:
            break


         # Menjaga agar database selalu diperbarui
        with open(PATH, 'w') as file:
            # Membuat objek writer
            writer = csv.writer(file, delimiter=";")
            # Menulis data ke dalam file csv
            writer.writerows(database.values())

if __name__ == "__main__":
    # Membersihkan tampilan user
    clear_screen()

     # Mengatur letak file database
    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/Warehouse_Inventory.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/Warehouse_Inventory.csv') 

    # Inisialisasi database
    database = initialize_db()

    # Menjalankan menu utama
    main()

