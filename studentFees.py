#Dylan Forde
#120309116

def test_question():
    filename = 'studentFees.txt' #sets filename as an easy variable to access
    inFile = open(filename, 'r') #opens file
    fees = {} #creates dictionary to add to later
    user_input = str(input('Please enter the name of a student: \n')) #takes input from user as a string, I did this early so that there is no need to run duplicate code if applicable
    total_fees_paid = 0 #gets ready to print the fees paid at the bottom
    for line in inFile: # for loop for each line in the file so i can extract the data
        student = line.split('\t') #split based on the fact entries separated by a tab
        if '\n' in student[2]: #easily gets rid of the \n jif it is present
            student[2] = student[2][:-1] # this gets rid of the \n at the end
        full_name = str(student[0]) + ' ' + str(student[1]) #makes it a string name rather than a list of two names
        total_fees_paid += int(student[2]) #adds the students fees paid so that an accurate total can be assessed at the end
        if full_name.lower() == user_input.lower(): #only runs the following code if the line is the student that they are looking for, helpful for when I have to print the name and value later on
            fees['name'] = full_name.title() #sets dict value equal to full name
            fees['value'] = int(student[2]) #adds the value from the list to the dictionary under value
        else:
            pass #not necessary but I think it looks easier to understand what is happening as the next line continues, which otherwise is not as clear as possible

    print('The fee paid by {name} is {value}'.format(**fees)) #prints the text put in
    print('The total fees paid: ' + str(total_fees_paid))



test_question()
def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
    rowTotals = []
    colTotals = []

    '''Calculate the score per row and append it to the rowTotals list'''
    for row in board:
        rowTotals.append(sum([value for key, value in symbols.items() if key in row]))
    
    rowTotals = [num if num>=0 else 0 for num in rowTotals]

    '''Calculate the score per column and append it to the colTotals list'''
    for column, number in enumerate(board):
        colTotals.append(sum([value for key, value in symbols.items() if key in column[number]]))

    return rowTotals, colTotals