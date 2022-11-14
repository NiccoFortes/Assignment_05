#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# NFortes, 2022-Nov-13, Added funtionalities to load data from text, delete line items, converted list of lists into a list of dictionaries.
#------------------------------------------#

# Declare variabls

strChoice = '' # User input from main menu
strChoiseD = '' # User iput for deleting items
Tbl1 = []  # list of lists to hold data
Tbl2 = []  # list for exporting data
Load1 =[]  # list for loading from file
dicRow = {}  # Dictionary row to append to list of disctionaries
dicRowLoad ={} # Variable for creating dictionary of loaded data
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # Loads data from text file as list and converts to dictionary and appends to main list of dictionaries.
       objFile = open(strFileName, 'r')
       for line in objFile:
           Load1.append(line.strip().split(','))
       for row in Load1:
           dicRowLoad ={'ID':int(row[0]),'Title':row[1],'Artist':row[2]}
           Tbl1.append(dicRowLoad)  
     
        
    elif strChoice == 'a':  
        #Add data to the table (2d-list) each time the user wants to add data
        
        #Code needs ID numbers to be unique to work. Code trusts user to input unique numbers, 
        #does not currently have functionallity to check against current list.
        strID = input('Enter an ID Number (must be unique): ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID':intID,'Title':strTitle,'Artist':strArtist}
        Tbl1.append(dicRow)
        
        
   
    elif strChoice == 'i':
        #Display the current data to the user each time the user wants to display the data
        print('ID | CD Title | Artist')
        for row in Tbl1:
            print(*row.values(), sep = '|', end = '\n')
            print()  
    
    elif strChoice == 'd':
        #Deletes an entry
        print('Please select which CD you want to delete from the table below by entering the corresponding ID')
        print('ID | CD Title | Artist')
        for row in Tbl1:
            print(*row.values(), sep = '|', end = '\n')
            print()
        print('Please enter ID to delete:')
        strChoiceD = int(input())
        index = 0
        #iterating through list to look into dictionaries. Removes dictionaries in list
        #by counting list indexies. Assumes ID numbers in dictionaries to be unique
        for dic in Tbl1:
            if dic['ID'] == strChoiceD:
                Tbl1.pop(index)
                break
            elif index == len(Tbl1)-1:
                print('Invalid selection, please chose another option')
                break
            else:
                index = index + 1
        
            
         
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in Tbl1:
            list1= list(row.values())
            Tbl2.append(list1)
            for row in Tbl2:
                strRow = ''
                for item in row:
                    strRow += str(item) + ','
                strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
      
    else:
        print('Please choose either l, a, i, d, s or x!')

