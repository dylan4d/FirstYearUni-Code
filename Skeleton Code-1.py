#Name: Dylan Forde
#Student ID: 120309116
#Programme: DSA

########################## Question 1a ############################################
def encrypt(w):

    vowels = {'a':0, 'e':1, 'i':2, 'o':2, 'u':3}

    '''Step 1 reverse the input e.g. if w is 'apple', it should be 'elppa' '''
    w = w[::-1] # reverses the order of the str using indexes. It goes from the end to the start using -1. [::] would not do this so -1 is needed to go backwards.

    '''Step 2 Replace all vowels using the dictionary provided e.g. elppa becomes 1lpp0 '''
    for vowel, value in vowels.items(): #for loop for the items in the dictionary, using the item method that lets us get both the key and value
        if vowel in w: #if statement that verifies to see if there are consonants in the word that need to be swapped out for the encrypted value. Using if else statement to filter this.
            w = w.replace(vowel, str(value)) #replace function that removes the key in the dictionary out of the saved variable and then replaces it with the value associated with the key
            #this then continues until there are no longer any keys left in the dictionary to loop through.

    '''Step 3 Add 'a5a' to the end of w e.g. 1lpp0a5a '''
    w = str(w + 'a5a') #string concatenation and also str() so that it is guaranteed a string although its unneccessary it makes it easier to visualise what the type of w is. 

    return w   #output should be 1lpp0a5a for an input of apple

word = input("Enter a single word: ")
encryptedWord = encrypt(word)
print (encryptedWord)

########################## Question 1b ############################################

def frame(w, h, c):
    if (w <= 2 or h <=2): #if statement using or in case w or h is 2 or below.
        print('Invalid') # prints Invalid because we would not be able to make it hollow if less than 2
        raise Exception('You cannot have less than or equal to two.') #raises error
    else: #if the values are above the minimum amount 
        for rows in range(1, h+1): #height dictates the number of rows and we go from 1 to height +1 in increments of 1 using a for loop
            for columns in range(1, w+1): #width dictates the number of columns and we go from 1 to width +1 in increments of one using a for loop
                if (rows == 1 or columns == 1) or (rows == h or columns == w): #we have to have different values for when row/column is the first or last row, as we want a border
                    print(c, end="") #print statement which prints the character we chose using end='' so that a newline isnt created.
                else: #else statement. 
                    print(" ", end="") #print statement which prints the hollow inside using end='' so that a newline is not created.
    
            print() #print(frame) does not have the output that is shown in the question. It calls the function so each line has <function frame xyzefnosefisiehf>.

width = int(input("Enter the width of the frame: "))
height = int(input("Enter the height of the frame: "))
character = input("Enter the character: ")
frame(width, height, character)

########################## Question 1c ############################################
def someFunction (L1):
    newList = []
    length = len(L1)
    counter = 0
    while counter < length:
        if L1[counter] > 5:
            newList.append(L1[counter])
        counter += 1
    return newList

#Your code here to rewrite with for loop - test
def someFunctionForLoop(L1): #defines function which takes list L1
    newlist = [] #creates a new list
    for num in L1: #iterates through the numbers in the list
        if num > 5: #if statement which executes if num is greater than 5
            newlist.append(num) # if num >5 then the num is added onto the end of the newlst created earlier
    return newlist #returns the newly created list

#Your code here to rewrite with as list comprehension - test
def someFunctionListComprehension(L1):
    return [num for num in L1 if num > 5] #list comprehension which adds num to list if when it goes through L1 it encounters a num greater than 5

print(someFunction([3, 4, 15, 7, 5, 6, 7]))
print(someFunctionForLoop([3, 4, 15, 7, 5, 6, 7]))
print(someFunctionListComprehension([3, 4, 15, 7, 5, 6, 7]))
########################## Question 1d ############################################
def totalEvenlyDivides (start, stop, divisor):
    total = 0 #sets total to add to later
    for num in range(start, stop+1): #iterates through list from range start to stop +1, plus one as it is not inclusive otherwise.
        if num % divisor == 0: #checks to make sure the divisor goes in with no remainder using mod
            total += num #updates the value held in total

    return total #returns the total after fully updated and finishing the loop

print (totalEvenlyDivides(1, 10, 2)) 
print (totalEvenlyDivides(1, 10, 3))
print (totalEvenlyDivides(2, 6, 25)) 

########################## Question 2 ############################################
def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
    rowTotals = [] #creates 2 lists to add to later
    colTotals = []
    colnums = []

    #Skipped this Question I couldnt get the column nums totalled and the row nums would not iterate over the dictionary multiple times in a line bad for last verification)
    #moved to question 4 instead
    '''Calculate the score per row and append it to the rowTotals list'''
    for row in board: #for loop so that it goes through each list
        rowTotals.append(sum([value for key, value in symbols.items() if key in row])) #append the sum of the rows to the rowtotals list
    
    rowTotals = [num if num>=0 else 0 for num in rowTotals] #reviews the previous list in order to ensure there are no neg numbers

    '''Calculate the score per column and append it to the colTotals list'''
    for positioncol, column in enumerate(board): # atm i cant seem to find out how to go over the columns 
        totalCol = 0 #sets the number to be added to later
        for positionrow, row in enumerate(board): # atm i cant seem to find out how to go voer the columns
            checkToSee = board[positionrow][positioncol] #gets the character at the position
            
            number = int(symbols[checkToSee]) # make the value a number
            totalCol += number #adds this to the totalCol
        colnums.append(number) #append the number

    indexes = len(colnums) #gets the length

    colTotals.append(sum(colnums[:indexes-1]))
    colTotals.append(sum(colnums[indexes-1:]))

    colTotals = [num if num>= 0 else 0 for num in colTotals]

    return rowTotals, colTotals

#rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
#print (rTotals, cTotals)
#rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])
#print (rTotals, cTotals)
'''rTotals, cTotals = calculate_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
print (rTotals, cTotals)'''

########################## Question 3 ############################################
def read_file (input_file):
    Users = {} #creates dictionary to add to later
    filename = input_file #sets filename to the filename input, not necessary but I prefer filename out of habit
    inFile = open(filename, 'r') #opens the file using read, this goes one line by one line
    for line in inFile: #for loop that loops through each line in the file
        line = line.strip('\n') #strips the \n if it is in the line (normally in the middle lines)
        line = line[1:-1] #gets rid of the () that are at the start and end of each line The parentheses would otherwise cause problems with splitting
        line = line.replace('"', '') # replaces "" that surround the address and names because they were formatted like '"item from list"' at the end. Was not sure if that was okay or not.
        line = line.split(", " ) #splits the lines based on ', ' so that we have lists without commas or spaces

        Users[int(line[0])] = line[1:] #sets the key to the dictionary as the int of the first element in the list(the numbers) and then sets the values of the dict as the rest of the list
    
    return Users

print(read_file ("details.txt"))

########################## Question 4 ############################################
def identifyPivot (L):
    left = 0 #sets the left side equal to 0 to add to later and verify vs the right side
    right = 0 #sets the right side equal to 0 to add to later and verify vs the left side

    for index in range(1, len(L)): #goes through all the numbers for the total of the list, then later subtracts to compare to left side
        right += L[index] #adds the number from the index position in list to right
    pivotCheck0= 0 #this checks the total from the left starts at 0 as index starts at 0
    pivotCheck1= 1 #this checkts the total fromt the right starts at 1 as it will be subtracting
    while pivotCheck1<len(L): #while the left side is less than the total from the right side, converges to the middle to find pivot
        right -= L[pivotCheck1] #-= subtracts from the number from the right to go towards pivot point
        left += L[pivotCheck0] #+= adds to the number from the left to go towards the pivot point

        if left == right: #if the pivot position is found
            pivot = L[pivotCheck0+1] #pivot position to the right of the left index that made the right and left sums equal.
            return pivot #as you have to get the pivot rather than the last number of the pivot from the left as it converges to center.
        
        pivotCheck0+=1 #tries the next number to see if that is equal next run
        pivotCheck1+=1 #tries the next number to see if that is equal next run

    
    return -1 #if there is not a pivot position returned then it returns -1

    return pivot #first pivot always encountered as starts from the right and then verifies from the left

print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0