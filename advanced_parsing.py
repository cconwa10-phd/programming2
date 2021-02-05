#ciara conway cconwa10@uncc.edu


aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}

# def creating_dict_transcription(filename): #takes in the file and creates dictionary
#     dict_file = {} #empty dictionary
#     dict_keys = [] #List of keys
#     dict_values = [] #List of values
#     with open(filename) as trans_file: #Opens file
#         for i, line in enumerate(trans_file): #iterates through transcription fasta file, assigns index
#             line = line.strip() #strips line
#             if i%2 != 0: #assigns values
#                 dict_values.append(line)
#             elif i%2 == 0: #assigns keys
#                 dict_keys.append(line)
#     #print(dict_values)
#     print(dict_keys)
#     # for i in range(0, len(dict_keys)): #creates dictionary
#     #     dict_file[dict_keys[i]] = dict_values[i]
#     # print(dict_file)
#     return dict_file #returns dictionary

def creating_dict_transcription(filename): #creates dictionary
    header_key = []
    seq_value = []
    file_dict = {}
    with open(filename) as trans_file: #opens file
        seq_temp_list = []
        for line in trans_file: #loops through lines
            if '>' in line: #isolates header
                line_new = line.strip()
                header_key.append(line_new) #appends line
                str_convert = ""
                for i in seq_temp_list: #loops through temp list
                    str_convert += i #converts to string
                seq_value.append(str_convert) #appends to list
                seq_temp_list.clear() #clears the list
            else:
                line_new = line.strip()
                seq_temp_list.append(line_new) #appends line if not header
        str_convert_end = ''
        for i in seq_temp_list: #loops through temp list
            str_convert_end += i #converts to string
        seq_value.append(str_convert_end) #appends to value
        seq_temp_list.clear() #clears temp list
    del seq_value[0] #deletes first place
    #print(seq_value)
    for i in range(len(header_key)): #converts to dictionary
        file_dict[header_key[i]] = seq_value[i]
    #print(file_dict)
    return file_dict #returns dictionary

# def start_codon_search(dictionary):
#     key_val_index = list()
#     for key, value in dictionary.items():
#         index_start_codon = []
#         for i in range(0,len(value)):
#             start_codon = value[i:i+3]
#             if start_codon == 'ATG':
#                 index_start_codon.append(i+4)
#         key_val_index.append((index_start_codon, key, value))
#     #print(key_val_index)
#     return key_val_index

# def start_codon_index(dictionary):
#     index_full = []
#     for key, value in dictionary.items():
#         index_start_codon = []
#         cycle = 0
#         for i in range(0, len(value)):
#             while cycle < 1:
#                 start_codon = value[i:i+3]
#                 if start_codon == 'ATG':
#                     index_start_codon.append((i+4, key, value))
#                     cycle += 1
#         index_full.append(index_start_codon)
#     print(index_full)
#     return index_full

def aa_amounts_search(dictionary, aa): #loops through dictionary and creates bias
    key = []
    value = []
    for key_d, value_d in dictionary.items(): #loops through dictionary of file
        value_list = []
        for key_a, value_a in aa.items(): #loops through aa dictionary
            key_list = []
            key_aa = []
            value_aa = []
            for j in value_a: #inner values of aa values
                count = 0
                for i in range(0, len(value_d), 3): #loops through the sequence in intervals of 3
                    single_codon = value_d[i:i+3] #codon is i - i+3
                    if single_codon == j: #if codon equals the codon from the aa dictionary
                        count += 1 #adds to count
                        key_list.append(key_a) #appends the amino acid name
                key_aa.append(j) #appends the amino acid codon
                value_aa.append(count) #appends the count
            aa_count = dict(zip(key_aa, value_aa)) #creates a dictionary between the keys and values
            for k, v in aa_count.items(): #for each item in the new aa count dicitonary
                if v != 0: #as long as the value isn't zero
                    aa_bias = v/len(key_list) #calculates the bias
                else:
                    aa_bias = v #else bias equals 0
                value_list.append((key_a, k, aa_bias)) #appends values the aa name, codon and count
            #print(value_list)
        key.append(key_d) #appends the key
        value.append(value_list) #appends the value
    print(key)
    print(value)
    return key, value #returns key and value

def create_aa_bias_dictionary(key, value): #creates a dicitonary
    dict_aa_bias = {}
    for i in range(len(key)): #This iterates to build out the key, value pairs
        dict_aa_bias[key[i]] = value[i]
    print(dict_aa_bias)
    return dict_aa_bias




def main():#main function, controls all functions defined
    filename = "/Users/ciaraconway/Desktop/Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa"
    file_dict = creating_dict_transcription(filename)
    aa_chart = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}
    # start_codon_search(file_dict)
    #start_codon_index(file_dict)
    key, value = aa_amounts_search(file_dict,aa_chart)
    create_aa_bias_dictionary(key, value)










if __name__ == "__main__":
	main()
