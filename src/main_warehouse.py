import mylib_warehouse as mylibw

# List of inventory data in dictionary form where values = SKU id, item name, current stock, brand, category
inventoryData = {
    "HI01" : ['HI01', "White Paint", 50, "Nippon", "Home Improvement"],
    "M01" : ["M01", "Wooden Plank", 100, "Lumber", "Materials"],
    "T01": ["T01", "Electric Drill", 75, "Krisbow", "Tools"]
}


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



    while True: 
        # Show main menu list to user
        print(menulist)

        # Ask user to input a number from main menu list
        option = mylibw.integer_validation("Please input option you want to select: ", minval = 1, maxval = 5)

        # Display function as the number inputted
        if option == 1:
            mylibw.show(inventoryData)
            
        elif option == 2:
                mylibw.add(inventoryData)

        elif option == 3:
            mylibw.updateInfo(inventoryData)

        elif option == 4:
            mylibw.delete(inventoryData)

        else:
            break

# Run the main program
main()

## test