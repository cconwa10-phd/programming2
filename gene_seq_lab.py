def try_except_base():
    while 1:  #Try/Except block to ensure valid options
        try:
            seq_input = [input("Please input your sequence\n")]
        except:
            print("This is not a valid answer, please re-enter entry")
            exit()
        else:
            if seq_input == ' ' : #Checks to see if age given is valid
                print("Contains invalid spaces, please revise")
            else:
                print("This is your input", seq_input)
                return seq_input


def complement_base_pairings(start_seq):
    compseq = ""
    invalidpositions = ""
    for i in range(0, len(start_seq)):
        if start_seq[i] == "A" or start_seq[i] == "a":
            compseq = compseq + "T"
        elif start_seq[i] == "T" or start_seq[i] == "t":
            compseq = compseq + "A"
        elif start_seq[i] == "C" or start_seq[i] == "c":
            compseq = compseq + "G"
        elif start_seq[i] == "G" or start_seq[i] == "g":
            compseq = compseq + "C"
        else:
            compseq += "N"
            invalidpositions += str(i) + ','
    print("Your original sequence is:" + start_seq)
    print("The complementary sequence is:" + compseq)
    print("Invalid bases found at positions" + invalidpositions)
    return compseq

def reverse_complement_base_pairings(comp_seq):
    reverse = comp_seq[:: 1]
    print(reverse)
    return reverse


def start_codon_base_pairings(codon_search):
    for i in range(0, len(codon_search)):
        if codon_search[i] == "A" or codon_search[i] == "a":
            if codon_search[i] == "T" or codon_search[i] == "t":
                if codon_search[i] == "G" or codon_search[i] == "g":
                    print("Codon sequence found:", i + 1, "to", i + 3 )
    return codon_search

def main(): #Main function that gives the flow of the program
    start_seq_input = try_except_base()
    complement_seq = complement_base_pairings(start_seq_input)
    reverse_seq = reverse_complement_base_pairings(complement_seq)
    start_codon_base_pairings(reverse_seq)






if __name__ == '__main__':
    main()
