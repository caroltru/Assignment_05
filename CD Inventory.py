#------------------------------------------#
# Title: CD Inventory.py
# Desc: Assignment05 script
# Change Log: (Who, When, What)
# Caroline Truong, 2021-Nov-13, Created File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Inventory
lstTbl = [{'ID': '1', 'CD Title':'The Big Wheel', 'Artist Name': 'Runrig'},
          {'ID': '2', 'CD Title':'Bad', 'Artist Name': 'Michael Jackson'},
          {'ID': '3', 'CD Title': '25', 'Artist Name': 'Adele'},
          {'ID': '4', 'CD TItle': 'ABBA', 'Artist Name': 'ABBA'}]
          
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        objfile = open(strFileName, 'r')
        for row in objfile:
            lstRow = row.strip().split(',')
            lstTbl.append(dicRow) 
            print("------------------")
            print(row)
        objfile.close()         
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD Title: ')
        strArtist = input('Enter the Artist Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    
    elif strChoice == 'd':
        print(lstTbl)
        selection = int(input('Which CD ID should be deleted?'))
        for selection in lstTbl:
            lstTbl.remove(selection)
            
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
        objFile.write(strRow)
        objFile.close()
    
    else:
        print('Please choose either l, a, i, d, s or x!')



