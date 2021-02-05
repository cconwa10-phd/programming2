#Ciara Conway, cconwa10@uncc.edu
def create_dict_months(): #This function will create the dictionary
    months = [["January", 31], ["February", 28],["March", 31],["April", 30],["May", 31],["June", 30],["July", 31],["August", 31],["September", 30],["October", 31],["November", 30],["December", 31]]
    key, value = map(list, zip(*months)) #This concatenates the two lists into the key and values of the dict
    dict_dates = {}
    for i in range(len(key)): #This iterates to build out the key, value pairs
        dict_dates[key[i]] = value[i]
    print(dict_dates)
    return dict_dates


def create_backward_dict(dictionary):
    old_dict = dictionary #This assigns the old dictionary
    new_dict = {} #have an empty dictionary
    for key, value in old_dict.items(): #This reverses the key and value pairs from the old dictionary
        new_dict[value] = key #Swaps the places
    print(new_dict)
    return new_dict #Returns the dictionary





def main(): #Main function that passes the two functions
    dictionary = create_dict_months()
    create_backward_dict(dictionary)

if __name__ == "__main__":
    main()
