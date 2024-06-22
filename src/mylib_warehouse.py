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
def alphaspace_validation(title):
    while True:
        itemName = input(title)
        if all(char.isalpha() or char.isspace() for char in itemName):
            break
        else:
            print("Please input only alphabets and spaces!")
    return itemName.title()


# A function used to check if the user input contains only alphabet, numbers, and spaces
def alnumspace_validation(title):
    while True:
        brandName = input(title)
        if all(char.isalpha() or char.isspace() or char.isnumeric() for char in brandName):
            break
        else:
            print("Please input only alphabets and spaces!")
    return brandName.title()


def email_validation(title):
    while True:
        email = input(title)
        if all(char.isalnum() or char == '.' or char == '@' for char in email):
            break
        else:
            print("Please input a valid email address (only alphabets, numbers, '.', and '@' are allowed)!")
    return email.lower()


# A function used to show database values in table format using tabulate
def showAll(database, header=["SKU_id", "Name", "Stock", "Brand", "Category"]):
    # Show data in table format
    print(tabulate(database.values(), headers=header, tablefmt="mixed_grid"))


# A function used to show database values based on its category
def showCat(database, category, header=['SKU_id', 'Name', 'Stock', 'Brand', 'Category']):
    foundItems = []
    for key, val in database.items():
        if val[4].lower()== category.lower():
            foundItems.append(val[:5])
    if foundItems == []:
        print(f'''\n No items were found in category {category}''')
    else:
        print(tabulate(foundItems, headers=header, tablefmt="mixed_grid"))


# A function used to show a particular item based on its SKU_id
def showItem(database, sku_id, header=["SKU_id", "Name", "Stock", "Brand", "Category", 'Supplier_id']):
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
            showInvent = {}
            for key, val in database.items():
                showInvent[key] = val[0:5]
            
            showAll(showInvent)

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
                itemName = alphaspace_validation('Enter item name: ')
                stock = integer_validation('Enter stock quantity: ')
                brand = alnumspace_validation('Enter brand name: ')
                category = categoryselection()
                supplierid = integer_validation('Enter supplier id: ')

                # Create a new item dictionary
                new_item= [sku_id, itemName, stock, brand, category, supplierid]
                databaseTemp = {}
                databaseTemp[sku_id] = new_item
                showAll(databaseTemp, header=["SKU_id", "Name", "Stock", "Brand", "Category", "Supplier_id"])
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
                stockDB[key] = [val[0], val[2], val[5]]
            
            showAll(stockDB, header=["SKU_id", "Stock", "Supplier_id"])
            
        elif showData == 2:
            stockDB = {}
            for key, val in database.items():
                if val[2] <= 15:
                    stockDB[key] = [val[0], val[2], val[5]]
                else:
                    continue
            
            showAll(stockDB, header=["SKU_id", "Stock", "Supplier_id"])

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
                itemName = alphaspace_validation('Enter item name: ')
                stock = integer_validation('Enter stock quantity: ')
                brand = alnumspace_validation('Enter brand name: ')
                category = categoryselection()
                supplier = integer_validation('Enter supplier id: ')

                # Create a new item dictionary
                update_item= [sku_id, itemName, stock, brand, category, supplier]
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


# A function to show suppliers information
def supplier(database1, database2):
    menulistsupplier = '''
    Supplier Information
    
    1. Show All Suppliers Contact Information
    2. Show Based on Supplier ID
    3. Add Supplier Contact Information
    4. Update Supplier Contact Information
    5. Delete Supplier Contact Information
    6. Back to Main Menu'''

    while True:
        print(menulistsupplier)
        suppOption = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 6)
        if suppOption == 1:
            # Show all supplier information data        
            showAll(database2, header= ['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])

        elif suppOption == 2:
            # Ask for supplier id
            suppId = integer_validation('Please input Supplier ID here: ', minval=0, maxval=(len(database2)-1))
            if suppId in database2:
                print(tabulate([database2[suppId]], headers =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'], tablefmt="mixed_grid"))
            else:
                print(f'\n Supplier with ID : {suppId} was not found in Supplier Information Data')

        elif suppOption == 3:
            # Choose add options
            submenu = '''
    Add New Supplier Contact Information?
    
    1. Add Data
    2. Back to Previous Menu'''

            while True:
                print(submenu)
                submenuopt = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)
                if submenuopt == 1:
                    # Ask user for supplier id 
                    supplier_id = integer_validation('please input supplier id: ')
                    if supplier_id in database2:
                        print('''\n Item already existed, please try again!''')
                    
                    elif supplier_id not in database2:
                        # If supplier_id is not in database
                        name = alphaspace_validation("Enter supplier's name: ")
                        contactPerson = alphaspace_validation("Enter contact person's name: ")
                        email = email_validation("Enter supplier's email: ")
                        country = alphaspace_validation("Enter supplier's country: ")

                        # Create a new item dictionary
                        new_supp= [supplier_id, name, contactPerson, email, country]
                        databaseTemp = {}
                        databaseTemp[supplier_id] = new_supp
                        showAll(databaseTemp, header =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                        saveData = integer_validation(f'''\n Do you want to save data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                        if saveData == 1:
                            # Add new supplier contact information to database
                            database2[supplier_id] = new_supp

                            print(f'\n Supplier with supplier id {supplier_id} have beem added successfully.')
                            break
                        else:
                            supplier(database2)

                elif submenuopt == 2:
                    break 

        elif suppOption == 4:
            # Update Supplier details
            updateSupp = '''
    Update Supplier Details?
    
    1. Update Supplier Details
    2. Back to Main Menu'''

            while True:
                print(updateSupp)
                optionUpdate = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)
                if optionUpdate == 1:
                    # Ask user for supplier_id
                    supp_id = integer_validation('please input supplier id: ')
                    if supp_id not in database2:
                        print('\n Supplier data does not exist, please try again!')

                    elif supp_id in database2:
                        # If supplier_id is in database
                        name = alphaspace_validation("Enter supplier's name: ")
                        contactPerson = alphaspace_validation("Enter contact person's name: ")
                        email = email_validation("Enter supplier's email: ")
                        country = alphaspace_validation("Enter supplier's country: ")

                        # Create a new item dictionary
                        update_item= [supp_id, name, contactPerson, email, country]
                        updateDB = {}
                        updateDB[supp_id] = update_item
                        showAll(updateDB, headers =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                        updateData = integer_validation(f'''\n Do you want to update data? 
            1. Yes
            2. No
            input:   ''', minval = 1, maxval = 2)
                        if updateData == 1:
                            # Add updated item to database
                            database2[supp_id] = update_item

                            print(f'\n Supplier data with id {supp_id} have been updated successfully.')
                            break
                        else:
                            supplier(database1, database2)

                elif optionUpdate == 2:
                    break

        elif suppOption == 5:
            delmenu = '''Delete Supplier's Information?

    1. Delete Supplier Info
    2. Back to Previous Menu'''

            while True:
                print(delmenu)
                delOpt = integer_validation("Please input the option you want to choose: ", minval=1, maxval=2)
                if delOpt == 1:
                    # Ask user for supplier id
                    suppid = integer_validation('Please input Supplier id that you want to delete: ')
                    if suppid not in database2:
                        print(f'\n Supplier information does not exist, please try again!')
                    
                    elif suppid in database2:
                        status = ''
                        for key, val in database1.items():
                            if suppid != val[5]:
                                status = 'No'
                            elif suppid == val[5]:
                                print(f'\n Supplier information is still being use, cannot delete supplier info!')
                                status = 'Yes'
                                break
                           
                        if status == 'No':
                            deleteDB = {}
                            deleteDB[suppid] = database2[suppid]
                            showAll(deleteDB, header =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                            deletesupp = integer_validation(f'''\n Do you want to delete supplier data?
            
            1. Yes
            2. No   ''', minval = 1, maxval = 2                                          )
    
                            if deletesupp == 1:
                                del database2[suppid]
                                print(f'\n Supplier data with id {suppid} have been deleted successfully.')
                                break
                            else:
                                supplier(database1, database2)

                elif delOpt == 2:
                    break

        else:
            break


