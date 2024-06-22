from tabulate import tabulate

# A function used to check if the user input contains only alphabets
def string_validation(title):
    while True:
        text = input(title)
        if text.isalpha() == True:
            break
        else:
            print("Please only input alphabet!")
    return text.title()


# A function used to check if the user input contains only number
def integer_validation(title, minval=0, maxval=100):
    while True:
        number = (input(title))
        try:
            number = int(number)
            if number >= minval and number <= maxval:
                break
            else:
                print("The number inputted is not in range, please try again.")
        except:
            print("Please input only numbers")
    return number
        

# A function used to check if the user input contains only number and alphabet
def alnum_validation(title):
    while True:
        alnumText = input(title)
        if alnumText.isalnum() == True:
            break
        else:
            print("Please input only alphabets and numbers!")
    return alnumText.upper()


# A function used to check if the user input contains only alphabet and spaces
def item_name_validation(title):
    while True:
        itemName = input(title)
        if all(char.isalpha() or char.isspace() for char in itemName):
            break
        else:
            print("Please input only alphabets and spaces!")
    return itemName.title()


# A function used to check if the user input contains only alphabet, numbers, and spaces
def brand_name_validation(title):
    while True:
        brandName = input(title)
        if all(char.isalpha() or char.isspace() or char.isnumeric() for char in brandName):
            break
        else:
            print("Please input only alphabets and spaces!")
    return brandName.title()


# A function used to show database values in table format using tabulate
def showAll(database, header=["SKU_id", "Name", "Stock", "Brand", "Category"]):
    # Show data in table format
    print(tabulate(database.values(), headers=header, tablefmt="mixed_grid"))


# A function used to show database values based on its category
def showCat(database, category, header=['SKU_id', 'Name', 'Stock', 'Brand', 'Category']):
    foundItems = []
    for key, val in database.items():
        if val[4].lower()== category.lower():
            foundItems.append(val)
    if foundItems == []:
        print(f'''\n No items were found in category {category}''')
    else:
        print(tabulate(foundItems, headers=header, tablefmt="mixed_grid"))


# A function used to show a particular item based on its SKU_id
def showItem(database, sku_id, header=["SKU_id", "Name", "Stock", "Brand", "Category"]):
    if sku_id in database:
        print(tabulate([database[sku_id]], headers = header, tablefmt="mixed_grid"))
    else:
        print(f'\n Item with SKU_id : {sku_id} was not found in inventory data')


# A function used to show different options of data
def show(database):

    menulist1 = '''
    Warehouse Inventory
    
    1. Show All Warehouse Inventory
    2. Show Based on Category
    3. Show Particular Item
    4. Back to Main Menu'''

    while True:
        print(menulist1)
        showData = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 4)
        if showData == 1:
            # Show all data
            showAll(database)
        elif showData == 2:
            # Ask for category
            category = categoryselection()
            showCat(database, category)
        elif showData == 3:
            # Ask for sku id
            sku_id = alnum_validation("Please input item's SKU id: ")
            showItem(database, sku_id)
        else:
            break


# A function for user to input which category they want to choose
def categoryselection():
    categoryList = """
    Please select one of the categories below!

    1. Home Improvement
    2. Materials
    3. Tools
    4. Gardening
    5. Furniture
    6. Cleaning
    7. Etc"""

    while True: 
        # show category list menu to user
        print(categoryList)

        # Ask user to input category selection number
        catSelection = integer_validation(title = "Input category number here: ", minval = 1, maxval = 7)

        if catSelection == 1:
            category = "Home Improvement"
            break
        elif catSelection == 2:
            category = "Materials"
            break
        elif catSelection == 3:
            category = "Tools"
            break
        elif catSelection == 4:
            category = "Gardening"
            break
        elif catSelection == 5:
            category = "Furniture"
            break
        elif catSelection == 6:
            category = "Cleaning"
            break
        else:
            category = "Etc"
            break
    return category


# A function used to add stock data to database
def add(database):

    menulist2 = '''
    Add Data to Warehouse Inventory?
    
    1. Add Data
    2. Back to Main Menu'''

    while True:
        print(menulist2)
        showData2 = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)
        if showData2 == 1:
            # Ask user for sku_id
            sku_id = alnum_validation('please input SKU id: ')
            if sku_id in database:
                option = integer_validation('''\n Item already existed, do you want to update item instead?
    1. Yes
    2. No 
    option: ''')
                if option == 1:
                    updateInfo(database)
                else:
                    add(database)

            if sku_id not in database:
                # If sku_id is not in database
                itemName = item_name_validation('Enter item name: ')
                stock = integer_validation('Enter stock quantity: ')
                brand = brand_name_validation('Enter brand name: ')
                category = categoryselection()

                # Create a new item dictionary
                new_item= [sku_id, itemName, stock, brand, category]
                databaseTemp = {}
                databaseTemp[sku_id] = new_item
                showAll(databaseTemp)
                saveData = integer_validation(f'''\n Do you want to save data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                if saveData == 1:
                     # Add new item to database
                    database[sku_id] = new_item

                    print(f'\n Item with SKU id {sku_id} have added successfully.')
                    break
                else:
                    add(database)

        elif showData2 == 2:
            break


# A function used to display stock info of items in warehouse
def stockInfo(database):

    menulist = '''
    See product stock information ?
    
    1. Show all product stock information
    2. Show items in low stock
    3. Back to Main Menu'''

    while True:
        print(menulist)
        showData = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 3)
        if showData == 1:
            stockDB = {}
            for key, val in database.items():
                stockDB[key] = [val[0], val[2]]
            
            showAll(stockDB, header=["SKU_id", "Stock"])
            
        elif showData == 2:
            stockDB = {}
            for key, val in database.items():
                if val[2] <= 10:
                    stockDB[key] = [val[0], val[2]]
                else:
                    continue
            
            showAll(stockDB, header=['SKU_id', 'Stock'])

        elif showData == 3:
            break


# A function used to update stock details to database
def updateInfo(database):

    menulist3 = '''
    Update Item Details?
    
    1. Update Item Details
    2. Back to Main Menu'''

    while True:
        print(menulist3)
        showData3 = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)
        if showData3 == 1:
            # Ask user for sku_id
            sku_id = alnum_validation('please input SKU id: ')
            if sku_id not in database:
                print('\n Item does not exist, please try again!')
                updateInfo(database)

            if sku_id in database:
                # If sku_id is in database
                itemName = item_name_validation('Enter item name: ')
                stock = integer_validation('Enter stock quantity: ')
                brand = brand_name_validation('Eenter brand name: ')
                category = categoryselection()

                # Create a new item dictionary
                update_item= [sku_id, itemName, stock, brand, category]
                databaseTemp2 = {}
                databaseTemp2[sku_id] = update_item
                showAll(databaseTemp2)
                updateData = integer_validation(f'''\n Do you want to update data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                if updateData == 1:
                     # Add new item to database
                    database[sku_id] = update_item

                    print(f'\n Item with SKU id {sku_id} have been updated successfully.')
                    break
                else:
                    updateInfo(database)

        elif showData3 == 2:
            break


# A function to delete an item in the database
def delete(database):

    menulist4 = '''Delete Item
    1. Delete an Item
    2. Back to Main Menu'''

    while True:
        print(menulist4)
        showData4 = integer_validation("Please input the option you want to choose: ", minval=1, maxval=2)
        if showData4 == 1:
            # Ask user for sku id
            sku_id = alnum_validation('Please input SKU id of item you want to delete: ')
            if sku_id not in database:
                print(f'\n Item does not exist, please try again!')
                delete(database)
            
            if sku_id in database:
                databaseTemp3 = {}
                databaseTemp3[sku_id] = database[sku_id]
                showAll(databaseTemp3)
                deleteData = integer_validation(f'''\n Do you want to delete data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                if deleteData == 1:
                    del database[sku_id]
                    print(f'\n Item with SKU id {sku_id} have been deleted successfully.')
                    break
                else:
                    delete(database)

        elif showData4 == 2:
            break