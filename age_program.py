#Ciara Conway, cconwa10@uncc.edu



def try_except():
    while 1:  #Try/Except block to ensure valid options
        try:
            age_input = int(input("Please input your age\n"))
        except ValueError:
            print("This is not a valid answer, please enter a number")
        else:
            if age_input < 0 or age_input > 150: #Checks to see if age given is valid
                print("Not a valid age, be realistic")
            else:
                return age_input

def age_program_while(): #while loop to run to the age of the input in addition to the next one
    age = try_except()
    age_null = 0
    while age_null <= int(age) + 1:
       if age_null == age + 1: #Runs if this is next birthday year
           age_milestone(age_null)
           print("May your next year of life be cool")
           age_null = age_null + 1
       else: #Runs all other ages
           age_milestone(age_null)
           age_null = age_null + 1

def age_program_for(): #For loop to run to the age of the input in addition to the next one
    age = try_except()
    for age_null in range(0, age + 2): #Have age +2 since it will run through age+1 with this range
        if age_null == age + 1:
           age_milestone(age_null) #Runs if this is next birthday year
           print("May your next year of life be cool")
        else:
           age_milestone(age_null) #Runs if this is next birthday year


def age_milestone(age_mile): #Function that contains all the milestones and prints each age, so everthing is printed on same line
    if age_mile == 0: #All milestones listed
        print(age_mile, "Congrats you have been born in to this cruel world.")
    elif age_mile == 5:
        print(age_mile, "Time to go to kindergarden, enjoy the next 12 years.")
    elif age_mile == 13:
        print(age_mile, "You are now a teenage, it's time to go through a 'phase'.")
    elif age_mile == 16:
        print(age_mile, "Driving is a privilege, so be careful!")
    elif age_mile == 18:
        print(age_mile, "New found independence, you can buy a lottery ticket now and start adulting.")
    elif age_mile == 21:
        print(age_mile, "You survived your teens and then some, time to celebrate with a drink!")
    elif age_mile == 25:
        print(age_mile, "Cue quarter-life crisis.")
    elif age_mile == 30:
        print(age_mile, "Happy 2nd 29th birthday ;).")
    elif age_mile == 40:
        print(age_mile, "Is that a gray hair, I see?")
    elif age_mile == 50:
        print(age_mile, "You are now enrolled in AARP")
    elif age_mile == 65:
        print(age_mile, "Hello Senior, hello retirement, and  hello 401K.")
    else: #Runs when there is not milestone associated
        print(age_mile)



def main(): #Main function that gives the flow of the program
    age_program_while()
    age_program_for()

if __name__ == '__main__':
    main()
