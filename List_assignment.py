#ciara conway, cconwa10@uncc.edu


import random as rm

def random_list(): #generates the list of random numbers
    random_num_list = list()
    cycles = 0
    while cycles < 20: #loop goes through iterations until 20 is hit
        random_num_range = rm.randint(1,100)
        random_num_list.append(random_num_range) #appends to a list
        cycles += 1 #increase cycle

    print(random_num_list)
    average = sum(random_num_list)/len(random_num_list) #calculates the average
    print(average)
    return random_num_list

def operations_on_list_low(list):
    list.sort() #sorts the list
    del list[0:2] #deletes the first two numbers that are the lowest
    print(list) #prints new list
    average_new = sum(list)/len(list) #calc new averate
    print("Average", average_new) #print average

def operations_on_list_high(list):
    list.sort() #sorts list
    del list[18:20] #deletes the last two numbers that are the highest
    print(list) #prints new list
    average_new = sum(list)/len(list) #new average
    print("Average", average_new)




def main(): #Main function that gives the flow of the program
    list = random_list()
    list_copy = list.copy() #copy of list to run through the other function
    operations_on_list_low(list)
    operations_on_list_high(list_copy)




if __name__ == '__main__':
    main()


