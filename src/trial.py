from tabulate import tabulate
import mylib_warehouse as mylibw

inventoryData = {
    "White Paint" : ['HI01', "White Paint", 50, "Nippon", "Home Improvement"],
    "Wooden Plank" : ["M01", "Wooden Plank", 100, "Lumber", "Materials"],
    "Electric Drill": ["T01", "Electric Drill", 75, "Krisbow", "Tools"]
}

option = mylibw.integer_validation('Please input the option you want to choose: ', minval=1, maxval = 7)
if option == 1 :
    print("option == 1")
    showData = mylibw.integer_validation('Please choose one of the options: ', minval = 0, maxval = 4)
    if showData == 1:
        mylibw.show(inventoryData)
    if showData == 2:



