#Ciara Conway, cconwa10@uncc.edu


import random as rm


def header_string(fastaHeader_input): # function returns gene + find, gene id + find, and protein id + find
	gene_label = fastaHeader_input[41:46]
	print("Gene Label:",gene_label) #gene
	gene_id_label = fastaHeader_input[81:84]
	print("Gene ID:",gene_id_label) #gene id
	protein_id_label = fastaHeader_input[223:234]
	print("Protein ID:",protein_id_label) #protein id

	return gene_label, gene_id_label, protein_id_label

def sequence_string(seqRecord_input): # Returns c and g, combined gc, complement seq, and reverse seq
	print(len(seqRecord_input))
	c = seqRecord_input.count("C")
	g = seqRecord_input.count("G")
	print(c,",", g) # c and g
	c_g = c + g
	print(c_g) #combined gc
	comp_seq = ""
	for i in range(0, len(seqRecord_input)): #for loop to create complement list
		if seqRecord_input[i] == "A":
			comp_seq = comp_seq + "T"
		elif seqRecord_input[i] == "T":
			comp_seq = comp_seq + "A"
		elif seqRecord_input[i] == "C":
			comp_seq = comp_seq + "G"
		elif seqRecord_input[i] == "G":
			comp_seq = comp_seq + "C"
	print(comp_seq)

	reverse_comp_seq = comp_seq[::-1] #generates reverse
	print(reverse_comp_seq)

	return c_g, reverse_comp_seq #returns the sequences to be called again if necessary


def user_input_num(): #This allows for the user to input the number of cycles or iterations for the mutation loop
    while 1:
        try:
            num_input = int(input("Please input your number of cycles for transversion and transition mutation simulation\n"))
        except:
            print("This is not a valid answer, please re-enter entry") #checks to make sure this is an integer input
        else:
            return num_input


def random_mutation(lower_seq, nucleotide): #Function has two parameters, the lower sequence from the Input_seq function and the position i
    new_base = '' #creates a string with the mutated or not mutated nucleotide depending on the random number
    prob_mutation = rm.randrange(1,5)
    if prob_mutation == 3 or prob_mutation == 4: #This is for transition mutations
        if lower_seq[nucleotide] == 'a':
            new_base = 'G'
        elif lower_seq[nucleotide] == 'g':
            new_base = 'A'
        elif lower_seq[nucleotide] == 't':
            new_base = 'C'
        elif lower_seq[nucleotide] == 'c':
            new_base = 'T'
    elif prob_mutation == 2 or prob_mutation == 5: #This is for transversion mutations
        purines = ['A', 'G']
        pyrimidines = ['C', 'T']
        transver_1 = rm.choice(purines)
        transver_2 = rm.choice(pyrimidines)
        if lower_seq[nucleotide] == 'a':
            new_base = transver_2
        elif lower_seq[nucleotide] == 't':
            new_base = transver_1
        elif lower_seq[nucleotide] == 'g':
            new_base = transver_2
        elif lower_seq[nucleotide] == 'c':
            new_base = transver_1
    else:
        new_base = lower_seq[nucleotide].upper() #returns the lower case sequence is the other two statements are not met, that way an empty string isn't returned
    return new_base #returns the new base to be called in another function


def Input_seq(sequence): #This function is used to manipulate the original sequence to a lower case and alter through calling the mutation function
    num = user_input_num()
    new_seq = sequence
    nucleotide = ['A', 'T', 'C', 'G'] #list used to check against the sequence give to see if valid
    new_base_list = [] # These 3 empty lists will append each mutation with the new base, old base, and the position of the mutation
    old_base_list = []
    mutation_list =[]
    for i in new_seq: #This for loop checks for a valid input, if there is an invalid base, the program exits
        if i not in nucleotide:
            exit()
    new_seq_lower = new_seq.lower() #new string assigned to the lower case version

    cycle = 0 #number of cycles will be used as a counter for the while loop, acting as the condition to run or break the loop
    while cycle < num:
        random_position = rm.randrange(0, len(new_seq_lower))
        for i in range(0, len(new_seq_lower)):
            if i == random_position: #runs through this if statement if i is equal to the random position selected above
                old_base = new_seq_lower[i]
                old_base_list.append(old_base)
                new_base = random_mutation(new_seq_lower, i) #runs the random_mutation function and returns the new base which can be appended to the list below
                new_base_list.append(new_base)
                mutation_point = i + 1
                mutation_list.append(mutation_point) #appends position to the mutation list
                new_seq_lower = new_seq_lower[:i] + new_base + new_seq_lower[i + 1:] #This new_seq_lower, builds out the new sequence with each iteration, only changing the specified base and keeping everything else the same
        cycle += 1 #increases the cycle by 1 each time to make a definite loop, not infinite
    print('mutations at:', mutation_list, '\nold bases:', old_base_list, '\nnew bases', new_base_list) #prints all the new and old bases and where the mutation may have occurred
    print('mutated sequence after', num, 'cycles:', new_seq_lower)
    new_seq_upper = new_seq_lower.upper() #prints the mutations in uppercase and rest of sequence as lower to see where changes occurred and how many cycles ran
    print('final sequence after', num, 'cycles:', new_seq_upper) #Gives the new sequence all upper
    return new_seq_upper

def main():
    fastaHeader = ">lcl|NG_005905.2_cds_NP_009225.1_1 [gene=BRCA1] [db_xref=CCDS:CCDS11453.1,GeneID:672,LRG:p1] [protein=breast cancer type 1 susceptibility protein isoform 1] [exception=annotated by transcript or proteomic data] [protein_id=NP_009225.1] [gbkey=CDS]"
    seqRecord = "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTG"
    header_string(fastaHeader)
    sequence_string(seqRecord)
    Input_seq(seqRecord)



if __name__ == "__main__":
	main()




