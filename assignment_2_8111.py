#ciara conway cconwa10@uncc.edu


import random as rm
aa_dicts = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}

def user_input_options(): #function takes the main user input
    choice = [1, 2, 3, 4] #list of choices
    while True: #while loop to run try and except loop
        try:
            user_input = int(input("Please choose from the following choices with 1 - 4:\nKeyword Search (1)\nAmino Acid Count (2)\nQuality Score (3)\nLeave (4)\n")) #options
        except ValueError: #checks to see if input is integer
            print("This is not a viable option, please select from the list")
        else:
            if user_input not in choice: #checks to see if choice is in choices
                print("This is not a viable option, please select 1 - 4")
            else:
                return user_input #returns user input
def user_input_aacount(): #function asks if keyword search should undergo aa count also
    choice = ["Yes", "No"] #list of choices
    while True: #while loop to run try and except loop
        try:
            user_input = input("Would you like to conduct an Amino Acid Count on your search results?\nPlease select Yes or No\n") #options
        except ValueError: #checks to see if input doesn't cause valueerror
            print("This is not a viable option, please select from the list")
        else:
            if user_input not in choice: #checks to see if choice is in choices
                print("This is not a viable option, please select Yes or No")
            else:
                return user_input #returns user input
def user_input_window(): #function asks for codon window and score window
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #list of choices
    while True: #while loop to run try and except loop
        try:
            user_input = int(input("Select the reading window index you want to read for codons or the width of score reading window\n0-10\n")) #options
        except ValueError: #checks to see if input is integer
            print("This is not a viable option, please select from the list")
        else:
            if user_input not in choice: #checks to see if choice is in choices
                print("This is not a viable option, please select 0-10")
            else:
                return user_input #returns user input

def user_input_score(): #function asks for the score threshold that should be read
    while True: #while loop to run try and except loop
        try:
            user_input = int(input("Select the score threshold you want to read for the score\n"))
        except ValueError:#checks to see if input is integer
            print("This is not a viable option, please select from the list")
        else:
            return user_input #returns user input

def user_create_file(): #asks if user wants to have an output file for keyword search and aacount
    choice = ["Yes", "No"] #list of choices
    while True: #while loop to run try and except loop
        try:
            print(choice)
            user_input = input("Would you like to save your results to a new file? please select between the two choices above:\n") #options
        except ValueError: #checks to see if input doesn't cause valueerror
            print("This is not a viable option, please select from the list")
        else:
            if user_input not in choice: #This statement checks to make sure the input is from the list and catches invalid inputs
                print("This is not a viable option, please select from the list")
            else:
                return user_input #returns user input

def parsing_file_list(filename): #parses file from original fastq file
    parsed_list = []
    result_list = []
    with open(filename) as file:
        for line in file: #creates parsed list from each line in file
            line = line.strip()
            parsed_list.append(line)
    for i in range(0, len(parsed_list), 4): #runs through the parsed list in intervals of four
        result_list.append((parsed_list[i], parsed_list[i+1], parsed_list[i+2], parsed_list[i+3])) #creates a nested list to a result list
    # print(result_list) #prints out the result list
    return result_list #returns the result list

def random_list_creation(result): #passes the result list and samples 5 random items from that list to be passed through aa count
    new_list = rm.sample(result, 5) #takes 5 random items from the list
    # print(new_list)
    return new_list #returns this new list

def keyword_search(file): #passes parsed file
    keyword_search_word = input("Please input the keyword you want to search\n") #asks user to enter keyword to search
    search_results = []
    search_results_string = ""
    for group in file: #runs through each item in the first set of nested list
        if keyword_search_word in group[0]: #checks to see if the keyword is in the first group of the inner nested list, or header
            search_results.append(group) #appends the result for the entire group so all four lines
            for i in group: #runs through the inner loop
                search_results_string += i + "\n" #appends to a string, used to generate a file if necessary
    print(search_results_string) #prints out the resulting string
    return search_results, search_results_string #returns the list and string

def create_aa_bias_dictionary(key, value): #creates a dictionary
    dict_aa_bias = {}
    for i in range(len(key)): #This iterates to build out the key, value pairs
        dict_aa_bias[key[i]] = value[i]
    print(dict_aa_bias)
    return dict_aa_bias #returns dictionary

def amino_acid_match(file, aa): #function that runs the amino acid match
    window = user_input_window() #asks the user for the codon window
    key = []
    value = []
    aa_count_string = ""
    for group in file: #runs throught the nested loop
        amino_acid_count = []
        amino_acid_string = ""
        for key_a, value_a in aa.items(): #runs through the key and values of the aa dictionary
            count = 0
            for i in range(int(window), len(group[1]), 3): #runs through the inner nest loop on the score item with the window as start point in intervals of 3
                single_codon = group[1][i:i+3] #single codon
                if single_codon in value_a: #matches values to the codon group
                    count += 1 #adds count
            amino_acid_count.append((key_a, count)) #appends the key and count that have been looped through
            amino_acid_string += key_a + ": " + str(count) + "\n" #creates a string version
        key.append(group[0]) #appends the header to the key list
        value.append(amino_acid_count) #appends the amino acid groups to the value list
        aa_count_string += str(group[0]) + "\n" + str(group[1]) + "\n" + str(group[2]) + "\n" + str(group[3]) + "\n" + amino_acid_string + "\n" #appends all values to a string to be written out to a file if chosen
    aa_dict_result = create_aa_bias_dictionary(key, value) #creates the dictionary
    print(aa_count_string)
    return aa_dict_result, aa_count_string #returns the dicitonary and string

def sequence_scoring(file): #function covers the sequence scoring
    window = user_input_window() #asks for reading window for score
    score_threshold = user_input_score() #asks for the score threshold
    new_file_string = ""
    new_list = []
    for group in file: #loops through the outer nested loop
        score_string = ""
        seq_string = ""
        for i in range(0, len(group[3]), int(window)): #loops through inner nested loop for the score and interval is the window given by user
            score_group = group[3][i:i+int(window)] #score group
            nucleotide_group = group[1][i:i+int(window)] #adjacent nucleotides
            score_window = []
            for j in score_group: #loops through the score group
                score_single = ord(j) - 64 #generates score for each item in score group
                score_window.append(score_single) #appends the score
            score_average = sum(score_window)/len(score_window) #takes the average
            if score_average >= score_threshold: #checks the score average against the threshold
                score_string += score_group #appends the group
                seq_string += nucleotide_group #appends the nucleotide group
            else: # once it doesn't  ends the appending
                #score_string += "*END" #appends an end
                #seq_string += "*END" #appends an end
                break #breaks the loop
        new_file_string += "\n" + str(group[0]) + "\n" + seq_string + "\n" + str(group[2]) + "\n" + score_string + "\n" #appends new scores and new nucleotide group in string
    #print(rm.sample(new_list, 5))
    return new_list, new_file_string #returns list and string

def write_out_results(result): #This function executeds the file to save out
    user_input_ask = user_create_file()
    if user_input_ask == "Yes": #If input from the save file choice is yes run
        file = "assignment2_trimmed.fastq" #inputs file name as the following
        out_file = open(file, "w") #Writes out the file with the results
        out_file.write(result)
        out_file.close() #closes file
        print("Outfile: ", file, " has been saved.")
    else:
        print("Ok, proceed")

def write_out_results_1_2(result): #This function executeds the file to save out
    user_input_ask = user_create_file()
    if user_input_ask == "Yes": #If input from the save file choice is yes run
        file = "assignment2_output.fastq" #goes through the input of the file via the try/except function
        out_file = open(file, "w") #Writes out the file with the results
        out_file.write(result)
        out_file.close() #closes file
        print("Outfile: ", file, " has been saved.")
    else:
        print("Ok, proceed")

def main():
    aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}
    filename = "/Users/ciaraconway/Desktop/assignment2v2.fastq" #filename
    file = parsing_file_list(filename) #function that parses file
    while True: #keeps running program
        user_input = user_input_options() #asks for input
        if user_input == 1: #keyword search
            result, string = keyword_search(file)
            print(result)
            search_input_results = user_input_aacount() #asks if keyword search file should undergo aa
            if search_input_results == "Yes":
                amino_count_result, amino_count_string = amino_acid_match(result, aa_dict)
                write_out_results_1_2(amino_count_string) #asks if user wants to write out file
            else:
                write_out_results_1_2(string) #asks if wants to write out keyword file
        elif user_input == 2: #aa count
            new_file = random_list_creation(file) #generates a random list
            result, string = amino_acid_match(new_file, aa_dict) #aa
            write_out_results_1_2(string) #writeout file
            print(result)
        elif user_input == 3: #score
            result, string = sequence_scoring(file)
            write_out_results(string) #writeout file
            print(result)

        elif user_input == 4: #leave the loop
            exit()

if __name__ == "__main__":
	main()
