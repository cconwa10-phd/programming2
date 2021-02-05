#ciara conway, cconwa10@uncc.edu


def user_input_search():
    choice = ["Gene ID", "GO ID", "Keyword", "Leave"] #These are the choice for the user search function
    while True:
        try:
            print(choice)
            user_input = input("Please specify what category you would like to search for\n")
        except ValueError:
            print("This is not a viable option, please select from the list")
        else:
            if user_input not in choice: #This statement checks to make sure the input is from the list and catches invalid inputs
                print("This is not a viable option, please select from the list")
            else:
                return user_input #returns user input to be called in other functions

def save_file_choice(): #Function that pulls in user input to see if they want to save to a new text file or not
    choice = ["Yes", "No"]
    while True:
        try:
            print(choice)
            user_input = input("Would you like to save your results to a new file? please select between the two choices above:\n")
        except ValueError:
            print("This is not a viable option, please select from the list")
        else:
            if user_input not in choice: #This statement checks to make sure the input is from the list and catches invalid inputs
                print("This is not a viable option, please select from the list")
            else:
                return user_input

def user_input_out_file(): #Function that accepts the user input for the file they want to save to
    while True:
        try:
            input_output_file = input("Please input the file name you want to save results to (keep under 50 characters please):\n")
        except IOError: #Checks if input file is a valid file
            print("Cannot open the file, invalid path or file name")
        else:
            if len(input_output_file) > 50: #Makes sure the length of the file doesn't exceed 50 characters
                print("Length of file exceeds limit, rename please")
            else:
                return input_output_file #returns the file output

def entire_user_input(): #This is the core function that will be called by the main function, depending on user input
    while True: #While loop allows for searches to continue until user selects leave
        user_input = user_input_search()
        if user_input == "Gene ID":
            result = Gene_ID()
            write_out_results(result)
        elif user_input == "GO ID":
            result = GO_ID()
            write_out_results(result)
        elif user_input == "Keyword":
            result = keyword()
            write_out_results(result)
        elif user_input == "Leave":
            exit() #once user chooses the leave option, loop breaks and code ends


def Gene_ID():
    filename = input("Please input the file you will be using\n") #asks for a viable filename to search with
    Gene_ID_search = input("Please input your Gene ID you want to search\n") #asks for the Gene Id you want to search
    result = ''
    with open(filename) as file: #Opens and closes the file with this statement, reads it in as default value
        for line in file:
            if line.startswith("Glyma"): #will ensure that only the lines that start with Glyma or valid data lines will be taken into account
                line_str = line.split("\t") #since each column is separated by tabs that is what we split on
                if Gene_ID_search in line_str[0]:
                    bp_desc = line_str[12] #Gives biological process
                    mf_desc = line_str[14] #Gives molecular function
                    cc_desc = line_str[16] #Gives cellular component
                    result += "Gene found " + Gene_ID_search + " in file:" #appends to the string with new lines in chunks
                    result += "\nBiological Process:" + bp_desc
                    result += "\nMolecular Function:" + mf_desc
                    result += "\nCellular Component:" + cc_desc + "\n"
                    print(result) #Prints out the results
    return result

def GO_ID(): #Allows the user to search for the GO Ids
    filename = input("Please input the file you will be using\n")
    Go_ID_search = input("Please input your GO ID you want to search\n")
    with open(filename) as file:
        for line in file:
            if line.startswith("Glyma"): #Each line that starts with glyma
                line_str = line.split("\t")
                if Go_ID_search in line_str[11]: #if the GO ID is found in one of the three columns, the column next to it is captured
                    bp_desc = line_str[12]
                    result = "Gene found " + Go_ID_search + " in file:"
                    result += "\nBiological Process:" + bp_desc
                    print(result)
                elif Go_ID_search in line_str[13]:
                    mf_desc = line_str[14]
                    result = "Gene found " + Go_ID_search + " in file:"
                    result += "\nMolecular Function:" + mf_desc
                    print(result)
                elif Go_ID_search in line_str[15]:
                    cc_desc = line_str[16]
                    result = "Gene found " + Go_ID_search + " in file:"
                    result += "\nCellular Component:" +cc_desc
                    print(result) #results are printed out
    return result #returns the results

def keyword(): #Allows for keyword search
    filename = input("Please input the file you will be using\n") #input the file being used
    keyword_search = input("Please input your keyword you want to search\n") #input the keyword to search
    line_number = 0
    with open(filename) as file:
        for line in file:
            line_number += 1 #Goes through the file line by line via the line number variable
            if keyword_search in line:
                result = keyword_search + " keyword found at line " + str(line_number) + "\nWith result line of:" + str(line.rstrip().split("\t")) + "\n"
                print(result) #The keyword is returned along with the line number and the resulting line

    return result

def write_out_results(result): #This function executeds the file to save out
    user_input_ask = save_file_choice()
    if user_input_ask == "Yes": #If input from the save file choice is yes run
        file = user_input_out_file() #goes through the input of the file via the try/except function
        out_file = open(file, "w") #Writes out the file with the results
        out_file.write(result)
        out_file.close() #closes file
        print("Outfile: ", file, " has been saved.")
    else:
        print("Ok, proceed") #if answer is no then prints the statement



def main(): #Main function that gives the flow of the program
    entire_user_input()




if __name__ == '__main__':
    main()
