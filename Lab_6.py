#Ciara Conway, cconwa10@uncc.edu
#Lab 6

import random

def user_input():#Try/Except Loop for User input
    while True:
        try:
            answer = input("Choose Yes or No\n")
        except ValueError:
            print("This is not a viable option, Yes or No")
        else:
            if answer != "Yes" and answer != "No":
                print("This is not a viable option, please choose Yes or No")
            else:
                return answer

def random_input(): #Random choice generator based on choices 0-10
    choice_program = random.randint(0,10)
    if choice_program == 0 or choice_program == 2 or choice_program == 4:
        print("Finding life and keeping your job was the least of your worries as a Mars sandstorm destroys the camp, \nwith devastating effects")
        print("Everyone is dead, except you, with no other options, you take an escape pod back to Earth")
        exit() #This causes the story to terminate if selected randomly
    elif choice_program == 1 or choice_program == 3:
        print("Whoa, intelligent life is already here on Mars! The Martians attack, taking everyone in the camp hostage.")
        print("You and your crew live the rest of your days as prisoners to a more sophisticated lifeform.")
        exit() #This causes the story to terminate if selected randomly
    else:
        print("You suddenly remember you forgot to eat lunch, and continue you what you were doing.")

def input_1(): #Input 1, allows for user to choose between two paths
    print("You are an Astrobiologist on an experimental expedition to Mars. \nYour goal is to find new life, study it, and then bring back to earth.")
    print("Would you like to accept this mission?")
    answer_1_input = user_input() #Pulls in the user_input function to match to the choice by user
    if answer_1_input == "Yes":
        print("Wonderful choice, it is your lucky day. While out foraging, the crew found promising samples. \nLooks like you've got work to do!")
    else:
        print("Probably the best choice you could have made, you are smart and have seen enough \nsci-fi movies to know this is not a good idea!")

def input_2(): #Input 2, allows for user to choose between two paths
    print("You culture the sample and find there are moving unicellular microbes, \nthe crew is excited and pressing you to further your results.")
    print("Would you like to add glucose growth serum to the cell culture?")
    answer_2_input = user_input() #Pulls in the user_input function to match to the choice by user
    if answer_2_input == "Yes":
        print("Whoa! Looks like the growth of the cells is beyond your expectations and are \nforming into something organized, complex.")
    else:
        print("You didn't fall to peer pressure and as a result have lost your job.  \nCongrats! You are going back to Earth.")

def input_3(): #Input 3, allows for user to choose between two paths
    print("You leave the new life form to grow, but it seems \nlike something sinister is occurring, it seems intelligent.")
    print("With the growth becoming uncontrollable, do you terminate the life form?")
    answer_3_input = user_input() #Pulls in the user_input function to match to the choice by user
    if answer_3_input == "No":
        print("Well, now the life form has escaped containment and is killing crew mates one after the other.")
    else:
        print("You may not get a Nobel Prize anytime soon, but you also just saved your crew mates")

def input_4(): #Input 4, allows for user to choose between two paths
    print("You are the last person alive from the expedition, \nthe only way to kill it is to shoot the life form off into deep space")
    print("Will you do anything necessary to expel the life form into deep space?")
    answer_4_input = user_input() #Pulls in the user_input function to match to the choice by user
    if answer_4_input == "Yes":
        print("You are successful in pushing the life form out into deep space, but the only way to accomplish was to also sacrifice yourself and accompany the life form into deep space.")
        print("So now you are dead and Earth may not know, but you saved everyone.... or did you? Was the life form so smart, it was able to make it to Earth?!")
        print("Cue suspenseful music")
        print("THE END")
    else:
        print("Since you have decided to stay on Mars, you will live your days in fear, constantly escaping the growing life form.")
        print("You will have to learn to grow potatoes and create water from O2 and H2, if not you will have enough supplies for 3 years")
        print("THE END")

def main(): #Main function that gives the flow of the program
    random_input()
    input_1()
    random_input()
    input_2()
    random_input()
    input_3()
    random_input()
    input_4()

if __name__ == '__main__':
    main()
