#ciara conway cconwa10@uncc.edu
import random as rm

def lottery_nums(): #generator function
    lottery_gen = rm.randint(1, 100) #generates a number 1 - 100
    yield lottery_gen #yield the value generated

def main(): # main function that loops through the generator function
    lott_cycle = 1 #accounts for the lottery slots
    while lott_cycle <= 6: #while loop that ends at the 6th slot
        for i in lottery_nums(): #iterates through the generator
            if lott_cycle == 6: #if it is the powerball
                print("Your powerball number is ", str(i)) #print this statement
                lott_cycle += 1 #add 1 to the lott_cycle
            else:
                print("Your slot ", lott_cycle, " lottery number is ", str(i)) #all other numbers print statement
                lott_cycle += 1 #add 1 to the lott_cycle



if __name__ == "__main__":
	main()
