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
def integer_validation(title, minval=1, maxval=999):
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
        

# A function used to check if the user input contains only numbers and alphabets
def alnum_validation(title):
    while True:
        alnumText = input(title)
        if alnumText.isalnum() == True:
            break
        else:
            print("Please input only alphabets and numbers!")
    return alnumText.upper()


# A function used to check if the user input contains only alphabets and spaces
def alphaspace_validation(title):
    while True:
        itemName = input(title)
        if all(char.isalpha() or char.isspace() for char in itemName):
            break
        else:
            print("Please input only alphabets and spaces!")
    return itemName.title()


# A function used to check if the user input contains only alphabets, numbers, and spaces
def alnumspace_validation(title):
    while True:
        alnumspace = input(title)
        if all(char.isalpha() or char.isspace() or char.isnumeric() for char in alnumspace):
            break
        else:
            print("Please input only alphabets and spaces!")
    return alnumspace.title()


# A function used to check if the email inputted by the user is valid or not
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


# A function used to show a particular item based of its SKU_id
def showItem(database, sku_id, header=["SKU_id", "Name", "Stock", "Brand", "Category", 'Supplier_id']):
    if sku_id in database:
        print(tabulate([database[sku_id]], headers = header, tablefmt="mixed_grid"))
    else:
        print(f'\n Item with SKU_id : {sku_id} was not found in inventory data')


# A function used to show different options of data
def show(database):

    # Sub Menu for Show function
    showmenu = '''
    Warehouse Inventory
    
    1. Show All Warehouse Inventory
    2. Show Based on Category
    3. Show Particular Item
    4. Show Stock Information
    5. Back to Main Menu'''

    while True:
        # Display sub menu
        print(showmenu)
        # Ask user to input option
        showData = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 5)

        # Show all warehouse inventory (Excluding supplier id column)
        if showData == 1:
            # Show all data
            showInvent = {}
            for key, val in database.items():
                showInvent[key] = val[0:5]

            # If database is empty
            if showInvent == {}:
                print(f'''\n No items in database, database is empty''')
            else:
                # Display data in table format
                showAll(showInvent)

        # Show warehouse inventory based on its category (Excluding supplier id column)
        elif showData == 2:
            # Ask user for category
            category = categoryselection()
            # Display data in table format
            showCat(database, category)

        # Show particular item information (Including supplier id column)
        elif showData == 3:
            # Ask user for sku id
            sku_id = alnum_validation("Please input item's SKU id: ")
            # Display data in table format
            showItem(database, sku_id)

        # Show Stock Information
        elif showData == 4:
            # Call stock information function
            stockInfo(database)

        # Break loop to go back to main menu
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

        # If function to return the intended category
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
def add(database1, database2):

    # Sub menu for Add function
    addmenu = '''
    Add Data to Warehouse Inventory?
    
    1. Add Data
    2. Back to Main Menu'''

    while True:
        # Show sub menu to user
        print(addmenu)
        # Ask for user input
        addData = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)
        if addData == 1:
            # Ask user for sku_id
            sku_id = alnum_validation('please input SKU id: ')
            # If sku_id already in database, ask user to update item instead
            if sku_id in database1:
                option = integer_validation('''\n Item already existed, do you want to update item instead?
    1. Yes
    2. No 
    option: ''', minval = 1, maxval = 2)
                # Redirect user to updateInfo function
                if option == 1:
                    updateInfo(database1)
                else:
                    continue

            # Create status variable for option processing
            status = ''       
            if sku_id not in database1:
                # If sku_id is not in database, ask user for product details
                itemName = alphaspace_validation('Enter item name: ')
                stock = integer_validation('Enter stock quantity: ')
                brand = alnumspace_validation('Enter brand name: ')
                category = categoryselection()

                # Validate if there are is already existing item
                # Create checkDB database to keep database values to be check
                duplicate_status = False
                # Input sku_id, name, brand, category from original database into checkDB
                for key, val in database1.items():
                    dbItemName, dbBrand, dbCategory = val[1], val[3], val[4]
                    # If data is found in database, show user the existing data
                    if dbItemName == itemName and dbBrand == brand and dbCategory == category:
                        print(f'\n Data already exist with SKU_id {key}, please try again!')
                        showItem(database1, sku_id = key)
                        duplicate_status = True
                        break

                if duplicate_status == True:
                    continue

                # If data has no duplicates, proceed with the function
                # Continue by asking for supplierid
                supplierid = integer_validation('Enter supplier id: ')
                        
                # Check if supplier id already exist
                if supplierid in database2:
                    # Create a new item dictionary
                    new_item= [sku_id, itemName, stock, brand, category, supplierid]
                    databaseTemp = {}
                    # Add new item to temporary database to confirm to user
                    databaseTemp[sku_id] = new_item
                    # Show temporary database to user
                    showAll(databaseTemp, header=["SKU_id", "Name", "Stock", "Brand", "Category", "Supplier_id"])
                    saveData = integer_validation(f'''\n Do you want to save data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
            
                    if saveData == 1:
                        # Add new item to database
                        database1[sku_id] = new_item
                        print(f'\n Item with SKU id {sku_id} have added successfully.')
                        break
                    # Go back to Add function sub menu
                    else:
                        continue
                
                # When supplier id does not exist, ask user to add supplier info
                elif supplierid not in database2:
                    while True:
                        askuser = integer_validation(f'''\nSupplier id has not been registered, do you want to add supplier's contact information first?
                                                            
    1. Yes
    2. No
    input:   ''', minval=1, maxval=2)
                        
                        # Proceed to add new supplier's contact information
                        if askuser == 1:
                            # Proceed to ask new supplier's details
                            name = alphaspace_validation("Enter supplier's name: ")
                            contactPerson = alphaspace_validation("Enter contact person's name: ")
                            email = email_validation("Enter supplier's email: ")
                            country = alphaspace_validation("Enter supplier's country: ")

                            # Create and add new supplier temporary dictionary
                            new_supp= [supplierid, name, contactPerson, email, country]
                            databaseTemp = {}
                            databaseTemp[supplierid] = new_supp
                            # Show and confirm to user about new supplier's details
                            showAll(databaseTemp, header =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                            saveData = integer_validation(f'''\n Do you want to save data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                                
                            # Add new supplier contact information to database
                            if saveData == 1:
                                database2[supplierid] = new_supp
                                print(f'\n Supplier with supplier id {supplierid} have been added successfully.')
                                status = 'Yes'
                                break
                            # Go back to supplier function
                            else:
                                status = 'No'
                                break
                        
                        elif askuser == 2:
                            break
                        
                        if status == 'Yes':      
                            # Create a new item dictionary
                            new_item= [sku_id, itemName, stock, brand, category, supplierid]
                            databaseTemp = {}
                            # Add new item to temporary database to confirm to user
                            databaseTemp[sku_id] = new_item
                            # Show temporary database to user
                            showAll(databaseTemp, header=["SKU_id", "Name", "Stock", "Brand", "Category", "Supplier_id"])
                            saveData = integer_validation(f'''\n Do you want to save data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
            
                            if saveData == 1:
                                # Add new item to database
                                database1[sku_id] = new_item
                                print(f'\n Item with SKU id {sku_id} have added successfully.')
                                break
                            # Go back to Add function sub menu
                            else:
                                continue

                        elif status == 'No':
                            break

        # Go back to main menu
        elif addData == 2:
            break


# A function used to display stock info of items in warehouse
def stockInfo(database):

    # Sub menu for Stock Info function
    stockmenu = '''
    See product stock information ?
    
    1. Show all product stock information
    2. Show items in low stock
    3. Back to Main Menu'''

    while True:
        # Show sub menu to user
        print(stockmenu)
        # Ask for user input
        stockData = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 3)

        # Show all product stock information (columns: SKU_id, Stock, and Supplier id)
        if stockData == 1:
            # Create a stock database to show to user
            stockDB = {}
            for key, val in database.items():
                stockDB[key] = [val[0], val[2], val[5]]
            # Display stock information in table format
            showAll(stockDB, header=["SKU_id", "Stock", "Supplier_id"])

        # Show products that are low in stock (<15 by default)    
        elif stockData == 2:
            # Create a stock database to show to  user
            stockDB = {}
            # Add low stock items to database
            for key, val in database.items():
                if val[2] <= 15:
                    stockDB[key] = [val[0], val[2], val[5]]
                else:
                    continue
            # Display low stock information in table format
            showAll(stockDB, header=["SKU_id", "Stock", "Supplier_id"])

        # Go back to main menu
        elif stockData == 3:
            break


# A function used to update stock details to database
def updateInfo(database):
    
    # Sub menu for Update Info function
    updatemenu = '''
    Update Item Details?
    
    1. Update Item Details
    2. Back to Main Menu'''

    while True:
        # Show sub menu to user
        print(updatemenu)
        # Ask for user input
        updateData = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)

        # Proceed to update item details
        if updateData == 1:
            # Ask user for sku_id
            sku_id = alnum_validation('please input SKU id: ')
            # Go back to submenu when sku_id does not exist
            if sku_id not in database:
                print('\n Item does not exist, please try again!')
                updateInfo(database)

            # If sku_id is in database
            if sku_id in database:
                # Create temporary DB to show item details to user
                wantUpdate = {}
                wantUpdate[sku_id] = database [sku_id]
                # Show and confirm to user if they want to continue updating
                showAll(wantUpdate)
                confirmUpdate = integer_validation(f'''\n Continue to update this data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                if confirmUpdate == 1:
                    # Proceed to ask for updated details
                    itemName = alphaspace_validation('Enter item name: ')
                    stock = integer_validation('Enter stock quantity: ')
                    brand = alnumspace_validation('Enter brand name: ')
                    category = categoryselection()

                    # Validate if there are is already existing item
                    # Create checkDB database to keep database values to be check
                    duplicate_status = False
                    # Input sku_id, name, brand, category from original database into checkDB
                    for key, val in database.items():
                        dbItemName, dbBrand, dbCategory = val[1], val[3], val[4]
                        # If data is found in database, show user the existing data
                        if dbItemName == itemName and dbBrand == brand and dbCategory == category:
                            print(f'\n Data already exist with SKU_id {key}, please try again!')
                            showItem(database, sku_id = key)
                            duplicate_status = True
                            break

                    if duplicate_status == True:
                        continue



                    # Proceed to ask supplier info
                    supplier = integer_validation('Enter supplier id: ')

                    # Create a temporary update info dictionary
                    update_item= [sku_id, itemName, stock, brand, category, supplier]
                    updateDB = {}
                    updateDB[sku_id] = update_item
                    # Show and confirm to user the inputted details
                    showAll(updateDB)
                    askupdateData = integer_validation(f'''\nDo you want to update data? 
1. Yes
2. No
input:   ''', minval = 1, maxval = 2)
                
                    if askupdateData == 1:
                        # Add new item to database
                        database[sku_id] = update_item
                        print(f'\n Item with SKU id {sku_id} have been updated successfully.')
                        break
                    # Go back to update info sub menu
                    else:
                        break

                # If user chooses 'No', go back to sub menu
                elif confirmUpdate == 2:
                    continue

        # Go back to main menu
        elif updateData == 2:
            break


# A function to delete an item in the database
def delete(database):

    # Sub menu for Delete function
    deletemenu = f'''\nDelete Item
    1. Delete an Item
    2. Back to Main Menu'''

    while True:
        # Show sub menu to user
        print(deletemenu)
        # Ask for user input
        deleteData = integer_validation("Please input the option you want to choose: ", minval=1, maxval=2)

        # Proceed with Delete Function
        if deleteData == 1:
            # Create a condition where delete more is True
            deleteMore = True
            
            # Create a new delete database to show item(s) that user wanted to delete
            deleteTempDB = {}

            # Create a looping condition when 'deleteMore' is True
            while deleteMore == True:

                # Ask user for sku id
                sku_id = alnum_validation('Please input SKU id of item you want to delete: ')
                # When sku id is not in database, go back to Delete sub menu
                if sku_id not in database:
                    print(f'\n Item does not exist, please try again!')
                    continue

                # When sku id is in database, proceed to show inputted item in a temporary database
                if sku_id in database:
                    deleteTemp = {}
                    deleteTemp[sku_id] = database[sku_id]
                    # Show and confirm item to delete to user
                    showAll(deleteTemp)
                    askdeleteData = integer_validation(f'''\n Do you want to delete this data? 
        1. Yes
        2. No
        input:   ''', minval = 1, maxval = 2)
                    # Proceed with the function
                    if askdeleteData == 1:
                        deleteTempDB [sku_id] = database[sku_id]
                        # Show user current items that they want to delete
                        showAll(deleteTempDB)
                        # Ask user if they want to delete more item
                        delMoreMenu = f'''\nDo you want to delete more item?
                        1. Yes
                        2. No''' 
                        print(delMoreMenu)
                        # Ask for user input
                        delMore = integer_validation("Please input the option you want to choose: ", minval=1, maxval=2)

                        # If user want to delete more, then
                        if delMore == 1:
                            deleteMore == True
                            continue
                        
                        # If user doesn't want to delete more items,
                        # proceed with deleting confirmed item(s) from original database
                        elif delMore == 2:
                            deleteMore == False
                            break

                    # Go back to Delete sub menu
                    else:
                        continue

            # Create a list to show deleted items
            deleteList = []
            # Delete confirmed item(s) from original database
            for key in deleteTempDB :
                del database[key]

            for key, val in deleteTempDB.items():
                deleteList.append(val[0])

            print(f'\n item(s) with SKU id: {deleteList} have been deleted successfully.')

        # Go back to main menu
        elif deleteData == 2:
            break


# A function to show all suppliers contact information
def allsuppliers(database2):
    # Show data in table format       
    showAll(database2, header= ['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])


# A function to show supplier's contact information based on supplier ID
def supplierid(database2):
    # Ask for supplier id
    suppId = integer_validation('Please input Supplier ID here: ', minval=0, maxval=999)
    # Show supplier id based on suppId
    if suppId in database2:
        print(tabulate([database2[suppId]], headers =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'], tablefmt="mixed_grid"))
    # Show notification that particular suppId was not found
    else:
        print(f'\n Supplier with ID : {suppId} was not found in Supplier Information Data')


# A function to add new supplier's contact information
def addsupplier(database2):
    # Sub menu to add supplier contact information
        addsubmenu = '''
    Add New Supplier Contact Information?
    
    1. Add Data
    2. Back to Previous Menu'''

        while True:
            # Show sub menu to user
            print(addsubmenu)
            # Ask for user input
            submenuopt = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)
            # Proceed with add supplier function
            if submenuopt == 1:
                # Ask user for supplier id 
                supplier_id = integer_validation('please input supplier id: ')

                # When supplier_id is already in database, tell user to try again
                if supplier_id in database2:
                    print('''\n Item already existed, please try again!''')

                # When supplier_id is not in database
                elif supplier_id not in database2:
                    # Proceed to ask new supplier's details
                    name = alphaspace_validation("Enter supplier's name: ")
                    contactPerson = alphaspace_validation("Enter contact person's name: ")
                    email = email_validation("Enter supplier's email: ")
                    country = alphaspace_validation("Enter supplier's country: ")

                    # Validate if there is already existing supplier info
                    # Create supp duplicate status
                    supp_duplicate_status = False
                    # Input sku_id, name, brand, category from original database into checkDB
                    for key, val in database2.items():
                        dbName, dbCP, dbEmail, dbCountry = val[1], val[2], val[3], val[4]
                        # If supplier data is found in database, show user the existing data
                        if dbName == name and dbCP == contactPerson and dbEmail == email and dbCountry == country:
                            print(f'\n Supplier data already exist with Supp_id {key}, please try again!')
                            showItem(database2, sku_id = key)
                            supp_duplicate_status = True
                            break

                    if supp_duplicate_status == True:
                        continue

                    # Create and add new supplier temporary dictionary
                    new_supp= [supplier_id, name, contactPerson, email, country]
                    databaseTemp = {}
                    databaseTemp[supplier_id] = new_supp
                    # Show and confirm to user about new supplier's details
                    showAll(databaseTemp, header =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                    saveData = integer_validation(f'''\n Do you want to save data? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                        
                    # Add new supplier contact information to database
                    if saveData == 1:
                        database2[supplier_id] = new_supp
                        print(f'\n Supplier with supplier id {supplier_id} have beem added successfully.')
                        break
                    # Go back to supplier function
                    else:
                        continue

            # Go back to previous menu
            elif submenuopt == 2:
                break 


# A function used to update suppliers contact information
def updatesupplier(database2):
    # Sub menu for Update Supplier function
    updateSupp = '''
Update Supplier Details?

1. Update Supplier Details
2. Back to Previous Menu'''

    while True:
        # Show sub menu to user
        print(updateSupp)
        # Ask for user input
        optionUpdate = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 2)

        # Proceed with Update Supplier option
        if optionUpdate == 1:
            # Ask user for supplier_id
            supp_id = integer_validation('please input supplier id: ')
            # Tell user to try again when supplier id is not in databse
            if supp_id not in database2:
                print('\n Supplier data does not exist, please try again!')

            # If supplier id is in database,
            elif supp_id in database2:
                # Create temporary supp DB to show item details to user
                suppUpdate = {}
                suppUpdate[supp_id] = database2[supp_id]
                # Show and confirm to user if they want to continue updating supplier contact information
                showAll(suppUpdate, header = ['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                confirmSuppUpdate = integer_validation(f'''\n Continue to update this supplier contact information? 
    1. Yes
    2. No
    input:   ''', minval = 1, maxval = 2)
                if confirmSuppUpdate == 1:    
                    # Ask for updated details
                    name = alphaspace_validation("Enter supplier's name: ")
                    contactPerson = alphaspace_validation("Enter contact person's name: ")
                    email = email_validation("Enter supplier's email: ")
                    country = alphaspace_validation("Enter supplier's country: ")

                    # Validate if there is already existing supplier info
                    # Create supp duplicate status
                    supp_duplicate_status = False
                    # Input sku_id, name, brand, category from original database into checkDB
                    for key, val in database2.items():
                        dbName, dbCP, dbEmail, dbCountry = val[1], val[2], val[3], val[4]
                        # If supplier data is found in database, show user the existing data
                        if dbName == name and dbCP == contactPerson and dbEmail == email and dbCountry == country:
                            print(f'\n Supplier data already exist with Supp_id {key}, please try again!')
                            showItem(database2, sku_id = key)
                            supp_duplicate_status = True
                            break

                    if supp_duplicate_status == True:
                        continue

                    # Create a new update temporary dictionary
                    update_item= [supp_id, name, contactPerson, email, country]
                    updateDB = {}
                    updateDB[supp_id] = update_item
                    # Show and confirm updated details to user
                    showAll(updateDB, header =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                    updateData = integer_validation(f'''\n Do you want to update data? 
        1. Yes
        2. No
        input:   ''', minval = 1, maxval = 2)
                    
                    # Add updated item to database
                    if updateData == 1:
                        database2[supp_id] = update_item
                        print(f'\n Supplier data with id {supp_id} have been updated successfully.')
                        break
                    # Go back to supplier function
                    else:
                        continue

                # If user chooses 'No', go back to sub menu
                if confirmSuppUpdate == 2:
                    continue

        # Go back to main menu
        elif optionUpdate == 2:
            break


# A function used to delete suppliers contact information
def deletesupplier(database1, database2):
    # Sub menu for Delete Supplier function
    delmenu = '''Delete Supplier's Information?

    1. Delete Supplier Info
    2. Back to Previous Menu'''

    while True:
        # Show sub menu to user
        print(delmenu)
        # Ask for user input
        delOpt = integer_validation("Please input the option you want to choose: ", minval=1, maxval=2)

        # Proceed with delete supplier option
        if delOpt == 1:
            # Ask user for supplier id
            suppid = integer_validation('Please input Supplier id that you want to delete: ')

            # Tell user to try again if the supplier id is not in database
            if suppid not in database2:
                print(f'\n Supplier information does not exist, please try again!')
            
            # If supplier id is in database,
            elif suppid in database2:
                status = ''
                # Make sure that the chosen supplier is not still being use in the other databse
                for key, val in database1.items():
                    if suppid != val[5]:
                        status = 'No'
                    # If it is still being use, then, user cannot delete supplier's information
                    elif suppid == val[5]:
                        print(f'\n Supplier information is still being use, cannot delete supplier info!')
                        status = 'Yes'
                        break
                
                # If it is not being use, then proceed with action
                if status == 'No':
                    # Create a temporary delete database to show user
                    deleteDB = {}
                    deleteDB[suppid] = database2[suppid]
                    # Show and confirm supplier details that will be deleted
                    showAll(deleteDB, header =['Supplier_id', 'Name', 'Contact_Person', 'Email', 'Country'])
                    deletesupp = integer_validation(f'''\n Do you want to delete supplier data?
    
    1. Yes
    2. No   ''', minval = 1, maxval = 2                                          )

                    # Proceed to delete supplier details from database
                    if deletesupp == 1:
                        del database2[suppid]
                        print(f'\n Supplier data with id {suppid} have been deleted successfully.')
                        break
                    # Go back to Supplier function
                    else:
                        continue

        # Go back to Previous menu
        elif delOpt == 2:
            break


# Main Supplier Function
def supplier(database1, database2):

     # Sub menu for Supplier function
    suppliermenu = '''
    Supplier Information
    
    1. Show All Suppliers Contact Information
    2. Show Based on Supplier ID
    3. Add Supplier Contact Information
    4. Update Supplier Contact Information
    5. Delete Supplier Contact Information
    6. Back to Main Menu'''

    while True:
        # Show sub menu to user
        print(suppliermenu)
        # Ask for user to choose option
        suppOption = integer_validation("Please input the option you want to select: ", minval = 1, maxval = 6)

        # Run function as the number inputted
        # Show all supplier contact information
        if suppOption == 1:
            allsuppliers(database2)

        # Show a particular supplier contact information
        elif suppOption == 2:
            supplierid(database2)

        # Function to add new supplier contact information
        elif suppOption == 3:
            addsupplier(database2)

        # Function to update suppliers contact information details
        elif suppOption == 4:
            updatesupplier(database2)

        # Function to delete suppliers contact information details
        elif suppOption == 5:
            deletesupplier(database1, database2)

        # Go back to main menu
        else:
            break

